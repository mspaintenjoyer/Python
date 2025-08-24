from concurrent import futures
import grpc
import banking_pb2_grpc
import banking_pb2
import time
from datetime import datetime

class AccountManager(banking_pb2_grpc.AccountManagementServicer):
    def __init__(self):
        self.accounts = {
            "user1": 1000.0,
            "user2": 500.0
        }
    
    def GetBalance(self, request, context):
        user_id = request.user_id
        if user_id not in self.accounts:
            context.abort(grpc.StatusCode.NOT_FOUND, "Account not found")
        return banking_pb2.BalanceResponse(
            user_id=user_id,
            balance=self.accounts[user_id]
        )
    
    def UpdateBalance(self, request, context):
        user_id = request.user_id
        amount = request.amount
        if user_id not in self.accounts:
            context.abort(grpc.StatusCode.NOT_FOUND, "Account not found")
        self.accounts[user_id] += amount
        return banking_pb2.BalanceResponse(
            user_id=user_id,
            balance=self.accounts[user_id]
        )

class TransactionProcessor(banking_pb2_grpc.TransactionServicer):
    def __init__(self, account_manager):
        self.account_manager = account_manager
        self.transactions = {}
    
    def InitiateTransfer(self, request, context):
        from_user = request.from_user
        to_user = request.to_user
        amount = request.amount
        
        if from_user not in self.account_manager.accounts:
            return banking_pb2.TransferResponse(
                status=banking_pb2.TransferResponse.TransferStatus.INVALID_ACCOUNT
            )
        
        if self.account_manager.accounts[from_user] < amount:
            return banking_pb2.TransferResponse(
                status=banking_pb2.TransferResponse.TransferStatus.INSUFFICIENT_FUNDS
            )
        
        transaction_id = f"txn-{time.time_ns()}"
        timestamp = datetime.now().isoformat()
        
        self.account_manager.accounts[from_user] -= amount
        self.account_manager.accounts[to_user] += amount
        
        self.transactions[transaction_id] = {
            "from": from_user,
            "to": to_user,
            "amount": amount,
            "timestamp": timestamp
        }
        
        return banking_pb2.TransferResponse(
            status=banking_pb2.TransferResponse.TransferStatus.SUCCESS,
            transaction_id=transaction_id,
            timestamp=timestamp
        )
    
    def GetTransactionHistory(self, request, context):
        user_id = request.user_id
        user_transactions = [
            txn for txn in self.transactions.values() 
            if txn["from"] == user_id or txn["to"] == user_id
        ]
        
        return banking_pb2.HistoryResponse(
            transactions=[
                banking_pb2.TransactionRecord(
                    transaction_id=txn_id,
                    counterparty=txn["to"] if txn["from"] == user_id else txn["from"],
                    amount=txn["amount"],
                    timestamp=txn["timestamp"]
                ) for txn_id, txn in self.transactions.items()
            ]
        )

def serve():
    account_manager = AccountManager()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    banking_pb2_grpc.add_AccountManagementServicer_to_server(account_manager, server)
    banking_pb2_grpc.add_TransactionServicer_to_server(
        TransactionProcessor(account_manager), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

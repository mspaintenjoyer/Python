import grpc
import banking_pb2_grpc
import banking_pb2

class BankingClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.account_stub = banking_pb2_grpc.AccountManagementStub(self.channel)
        self.transaction_stub = banking_pb2_grpc.TransactionStub(self.channel)
    
    def get_balance(self, user_id):
        try:
            response = self.account_stub.GetBalance(
                banking_pb2.GetBalanceRequest(user_id=user_id)
            )
            return response.balance
        except grpc.RpcError as e:
            print(f"Error: {e.code()}")
            return None
    
    def transfer(self, from_user, to_user, amount):
        response = self.transaction_stub.InitiateTransfer(
            banking_pb2.TransferRequest(
                from_user=from_user,
                to_user=to_user,
                amount=amount
            )
        )
        return response
    
    def get_transaction_history(self, user_id):
        response = self.transaction_stub.GetTransactionHistory(
            banking_pb2.HistoryRequest(user_id=user_id)
        )
        return response.transactions

if __name__ == "__main__":
    client = BankingClient()
    
    # Example usage
    print("User1 balance:", client.get_balance("user1"))
    print("Transferring $100 from user1 to user2")
    transfer_response = client.transfer("user1", "user2", 100)
    if transfer_response.status == banking_pb2.TransferResponse.TransferStatus.SUCCESS:
        print("Transfer successful!")
        print("New balances:")
        print("User1:", client.get_balance("user1"))
        print("User2:", client.get_balance("user2"))
        print("\nTransaction History:")
        for txn in client.get_transaction_history("user1"):
            print(f"{txn.timestamp}: {txn.amount} to {txn.counterparty}")

# Python
This project is a Python gRPC-based banking service that simulates simple account management and money transfer operations. It defines two core services:

Account Management Service – provides operations to check and update user balances.

Transaction Service – handles fund transfers between accounts and maintains transaction history.

The backend is implemented in Python with gRPC, where the server (server.py) manages user accounts and processes transactions, while the client (client.py) communicates with the server to fetch balances, initiate transfers, and retrieve transaction history.

For testing and interaction, the system can also be accessed via Flask endpoints or cURL commands, making it easy to integrate with external tools or quickly test requests.

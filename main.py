from blockchain import *


def main():
    # Create a blockchain
    blockchain = Blockchain()

    transaction1 = {"sender": "Alice", "receiver": "Bob", "amount": 10}
    transaction2 = {"sender": "Bob", "receiver": "Charlie", "amount": 5}
    transaction3 = {"sender": "Charlie", "receiver": "Alice", "amount": 15}

    # Add some transactions to the blockchain
    blockchain.add_new_transaction(transaction1)
    blockchain.add_new_transaction(transaction2)
    blockchain.add_new_transaction(transaction3)

    # Mine a new block
    print("Mining a new block...")
    last_block_hash = blockchain.mine(difficulty=2)
    print(f"Block mined: {last_block_hash}")

    # Print the current state of the blockchain
    print("Current blockchain:")
    for i, block in enumerate(blockchain.chain):
        print(f"Block {i}:")
        print(f"Hash: {block.hash}")
        print(f"Transactions: {block.transactions}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Previous hash: {block.previous_hash}")


if __name__ == "__main__":
    main()

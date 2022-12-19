# Blockchain in Python

#### This project is a simple implementation of a blockchain in Python. It includes a Block class that represents a block in the chain and a Blockchain class that represents the entire chain.

## Getting Started

To use the code, you will need to have Python 3 installed on your machine.

## How to Use

To create a new blockchain, you can use the following code:

 `blockchain = Blockchain()`
 
 To add new transactions to the blockchain, you can use the add_new_transaction method:
 
 ```
transaction1 = {"sender": "Alice", "receiver": "Bob", "amount": 10}
transaction2 = {"sender": "Bob", "receiver": "Charlie", "amount": 5}
transaction3 = {"sender": "Charlie", "receiver": "Alice", "amount": 15}

blockchain.add_new_transaction(transaction1)
blockchain.add_new_transaction(transaction2)
blockchain.add_new_transaction(transaction3)

 ```
 
 To mine a new block, you can use the mine method:
 
 `last_block_hash = blockchain.mine(difficulty=2)`
 
The mine method will add the pending transactions to the blockchain and find a valid proof of work (also known as mining). The difficulty parameter controls the mining speed.

To check the validity of the blockchain, you can use the is_valid_proof method:

`blockchain.is_valid_proof(block, block_hash)`



### Feel free to fork this repository and try it on your local machine

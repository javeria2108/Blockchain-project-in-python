# Simple Blockchain Implementation in Python

This project demonstrates a basic blockchain implementation using Python and Flask. The blockchain supports mining new blocks, adding transactions, and viewing the blockchain.

## Features

- **Mine Blocks**: Generate new blocks by solving a proof of work algorithm.
- **Add Transactions**: Create new transactions that will be added to the next mined block.
- **View Blockchain**: Retrieve the full blockchain and pending transactions.
- **Register Nodes**: Add new nodes to the network.

## Requirements

- Python 3.11 or higher
- Flask

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/blockchain-python.git
    cd blockchain-python
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install Flask
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **API Endpoints:**

    - **Mine Block**
        - **URL**: `/mine_block`
        - **Method**: `GET`
        - **Description**: Mines a new block and adds it to the blockchain.
        - **Response**: Details of the mined block.
        
        ```json
        {
            "message": "A block is MINED",
            "index": 2,
            "timestamp": 1625074762.851,
            "proof": 35293,
            "previous_hash": "abc123...",
            "transactions": [{"sender": "sender", "recipient": "node_identifier", "amount": "10BTC"}]
        }
        ```

    - **Create Transaction**
        - **URL**: `/transactions/new`
        - **Method**: `POST`
        - **Description**: Adds a new transaction to the list of pending transactions.
        - **Body**: JSON containing `sender`, `recipient`, and `amount`.
        - **Response**: Confirmation message.
        
        ```json
        {
            "message": "Transaction will be added to next Block"
        }
        ```

    - **View Blockchain**
        - **URL**: `/get_chain`
        - **Method**: `GET`
        - **Description**: Retrieves the current blockchain and pending transactions.
        - **Response**: The full blockchain and pending transactions.
        
        ```json
        {
            "chain": [...],
            "pending_transactions": [...],
            "length": 1
        }
        ```

    - **Register Nodes**
        - **URL**: `/nodes/register`
        - **Method**: `POST`
        - **Description**: Registers new nodes to the blockchain network.
        - **Body**: JSON containing `nodes` (list of node addresses).
        - **Response**: Confirmation message.
        
        ```json
        {
            "message": "New nodes have been added",
            "total_nodes": [...]
        }
        ```

## Code Overview

### Blockchain Class

- **`__init__`**: Initializes the blockchain with the genesis block.
- **`new_block`**: Creates a new block and adds it to the chain.
- **`last_block`**: Returns the last block in the chain.
- **`new_transaction`**: Adds a new transaction to the list of pending transactions.
- **`hash`**: Hashes a block.
- **`proof`**: Proof of work algorithm.

### Flask Endpoints

- **`/mine_block`**: Mines a new block.
- **`/transactions/new`**: Creates a new transaction.
- **`/get_chain`**: Returns the blockchain.
- **`/nodes/register`**: Registers new nodes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

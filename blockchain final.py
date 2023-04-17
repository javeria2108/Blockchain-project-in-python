import hashlib
import json 
from flask import Flask,jsonify,request
from time import time
from uuid import uuid4
class Blockchain():
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(proof=1,previous_hash='GENESISBLOCK')
    def new_block(self, proof, previous_hash):
            block = {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'transactions': self.pending_transactions,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1]),
            }
            self.pending_transactions = []
            self.chain.append(block)
            return block    
    @property
    def last_block(self):
            return self.chain[-1]
    def new_transaction(self, sender, recipient, amount):
            transaction = {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
            self.pending_transactions.append(transaction)
            return self.last_block['index'] + 1
    def hash(self, block):
            string_object = json.dumps(block, sort_keys=True)
            block_string = string_object.encode()
            raw_hash = hashlib.sha256(block_string)
            hex_hash = raw_hash.hexdigest()
            return hex_hash
    def proof(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1     
        return new_proof  
nodes=set()
app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.chain[-1]
    previous_proof = previous_block['proof']
    proof = blockchain.proof(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.new_transaction("sender",node_identifier,"10BTC") 
    block = blockchain.new_block(proof, previous_hash)
    response = {'message': 'A block is MINED',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions':block['transactions']} 
    return jsonify(response), 200
@app.route('/transactions/new',methods=['POST'])
def new_transactions():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400


    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message':'Transaction will be added to next Block'}
    return jsonify(response), 200
@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'pending_transactions':blockchain.pending_transactions,
                'length': len(blockchain.chain)}
    return jsonify(response), 200 
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    new_nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in new_nodes:
        nodes.add(node)
    response ={'message':'new nodes have been added',
               'chain': blockchain.chain,
               'pending_transactions':blockchain.pending_transactions,
                'length': len(blockchain.chain)}    
    return jsonify(response),200
app.run(host='127.0.0.1', port=5000)

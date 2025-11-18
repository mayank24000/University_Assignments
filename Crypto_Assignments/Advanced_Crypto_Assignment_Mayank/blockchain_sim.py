"""
Q4: Blockchain Cryptography Simulation
Demonstrates blockchain fundamentals including hashing, digital signatures,
Merkle trees, and consensus mechanisms
"""

import hashlib
import json
import time
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import base64


class MerkleTree:
    """Implements Merkle Tree for efficient transaction verification"""
    
    def __init__(self, transactions):
        self.transactions = transactions
        self.tree = self.build_tree()
        self.root = self.tree[-1][0] if self.tree else None
    
    def hash_data(self, data):
        """Hash a single piece of data"""
        return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()
    
    def build_tree(self):
        """Build Merkle tree from transactions"""
        if not self.transactions:
            return []
        
        # Level 0: Hash all transactions
        current_level = [self.hash_data(tx) for tx in self.transactions]
        tree = [current_level.copy()]
        
        # Build tree bottom-up
        while len(current_level) > 1:
            next_level = []
            
            # Process pairs
            for i in range(0, len(current_level), 2):
                if i + 1 < len(current_level):
                    combined = current_level[i] + current_level[i + 1]
                else:
                    # Odd number: duplicate last hash
                    combined = current_level[i] + current_level[i]
                
                next_level.append(self.hash_data(combined))
            
            tree.append(next_level)
            current_level = next_level
        
        return tree
    
    def get_proof(self, transaction_index):
        """Get Merkle proof for a transaction"""
        if transaction_index >= len(self.transactions):
            return None
        
        proof = []
        index = transaction_index
        
        for level in self.tree[:-1]:  # Exclude root
            if index % 2 == 0:
                # Left node: need right sibling
                if index + 1 < len(level):
                    proof.append(('R', level[index + 1]))
                else:
                    proof.append(('R', level[index]))  # Duplicate
            else:
                # Right node: need left sibling
                proof.append(('L', level[index - 1]))
            
            index = index // 2
        
        return proof
    
    def verify_proof(self, transaction, proof, root):
        """Verify Merkle proof"""
        current_hash = self.hash_data(transaction)
        
        for direction, sibling_hash in proof:
            if direction == 'L':
                combined = sibling_hash + current_hash
            else:
                combined = current_hash + sibling_hash
            current_hash = self.hash_data(combined)
        
        return current_hash == root


class Block:
    """Represents a single block in the blockchain"""
    
    def __init__(self, index, transactions, previous_hash, difficulty=4):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.merkle_tree = MerkleTree([json.dumps(tx, sort_keys=True) for tx in transactions])
        self.merkle_root = self.merkle_tree.root
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Calculate block hash"""
        block_data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'merkle_root': self.merkle_root,
            'nonce': self.nonce
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self):
        """Proof of Work mining"""
        target = '0' * self.difficulty
        print(f"Mining block {self.index} (difficulty: {self.difficulty})...", end='', flush=True)
        start_time = time.time()
        
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        elapsed = time.time() - start_time
        print(f" Mined! (nonce: {self.nonce}, time: {elapsed:.2f}s)")
        return self.hash
    
    def to_dict(self):
        """Convert block to dictionary"""
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'datetime': datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'merkle_root': self.merkle_root,
            'nonce': self.nonce,
            'hash': self.hash
        }


class DigitalWallet:
    """Manages cryptographic keys for blockchain transactions"""
    
    def __init__(self, owner):
        self.owner = owner
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.address = self.generate_address()
    
    def generate_address(self):
        """Generate wallet address from public key"""
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        address_hash = hashlib.sha256(public_pem).hexdigest()
        return address_hash[:40]  # Bitcoin-style address
    
    def sign_transaction(self, transaction):
        """Sign transaction with private key"""
        transaction_string = json.dumps(transaction, sort_keys=True)
        signature = self.private_key.sign(
            transaction_string.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()
    
    def verify_transaction(self, transaction, signature, public_key):
        """Verify transaction signature"""
        try:
            transaction_string = json.dumps(transaction, sort_keys=True)
            signature_bytes = base64.b64decode(signature)
            public_key.verify(
                signature_bytes,
                transaction_string.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False


class Blockchain:
    """Blockchain implementation with Proof of Work consensus"""
    
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = 50
        self.wallets = {}
        
        # Create genesis block
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Create the first block"""
        genesis_block = Block(0, [{
            'from': 'genesis',
            'to': 'network',
            'amount': 0,
            'timestamp': time.time()
        }], '0', self.difficulty)
        genesis_block.mine_block()
        self.chain.append(genesis_block)
        print("✓ Genesis block created")
    
    def get_latest_block(self):
        """Get the most recent block"""
        return self.chain[-1]
    
    def add_transaction(self, transaction, signature, sender_wallet):
        """Add a signed transaction to pending pool"""
        # Verify signature
        if not sender_wallet.verify_transaction(transaction, signature, sender_wallet.public_key):
            print("✗ Invalid transaction signature")
            return False
        
        transaction['signature'] = signature
        self.pending_transactions.append(transaction)
        print(f"✓ Transaction added: {transaction['from'][:8]}... → {transaction['to'][:8]}... ({transaction['amount']} coins)")
        return True
    
    def mine_pending_transactions(self, miner_address):
        """Mine a new block with pending transactions"""
        if not self.pending_transactions:
            print("No transactions to mine")
            return False
        
        # Add mining reward transaction
        reward_tx = {
            'from': 'network',
            'to': miner_address,
            'amount': self.mining_reward,
            'timestamp': time.time(),
            'signature': 'mining_reward'
        }
        
        transactions = self.pending_transactions + [reward_tx]
        
        # Create and mine new block
        new_block = Block(
            len(self.chain),
            transactions,
            self.get_latest_block().hash,
            self.difficulty
        )
        new_block.mine_block()
        
        # Add to chain
        self.chain.append(new_block)
        self.pending_transactions = []
        
        print(f"✓ Block {new_block.index} added to chain")
        return new_block
    
    def validate_chain(self):
        """Validate entire blockchain"""
        print("\nValidating blockchain...")
        
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check hash
            if current_block.hash != current_block.calculate_hash():
                print(f"✗ Block {i} hash is invalid")
                return False
            
            # Check link to previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"✗ Block {i} is not properly linked")
                return False
            
            # Check proof of work
            if current_block.hash[:self.difficulty] != '0' * self.difficulty:
                print(f"✗ Block {i} does not meet difficulty requirement")
                return False
        
        print("✓ Blockchain is valid")
        return True
    
    def demonstrate_tampering(self):
        """Show that tampering is detectable"""
        if len(self.chain) < 2:
            print("Need at least 2 blocks to demonstrate tampering")
            return
        
        print("\n" + "="*70)
        print("TAMPER-PROOFING DEMONSTRATION")
        print("="*70)
        
        # Show original state
        print("\nOriginal blockchain is valid:")
        self.validate_chain()
        
        # Tamper with a block
        print(f"\n⚠ Attempting to tamper with block 1...")
        original_amount = self.chain[1].transactions[0]['amount']
        self.chain[1].transactions[0]['amount'] = 999999
        print(f"  Changed transaction amount: {original_amount} → 999999")
        
        # Show detection
        print("\nValidating tampered blockchain:")
        self.validate_chain()
        
        # Restore
        self.chain[1].transactions[0]['amount'] = original_amount
        print(f"\n✓ Restored original value: {original_amount}")
    
    def get_balance(self, address):
        """Calculate balance for an address"""
        balance = 0
        
        for block in self.chain:
            for tx in block.transactions:
                if tx['to'] == address:
                    balance += tx['amount']
                if tx['from'] == address:
                    balance -= tx['amount']
        
        return balance
    
    def display_chain(self):
        """Display the entire blockchain"""
        print("\n" + "="*70)
        print("BLOCKCHAIN STATE")
        print("="*70)
        
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"  Timestamp: {datetime.fromtimestamp(block.timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  Hash: {block.hash}")
            print(f"  Previous: {block.previous_hash}")
            print(f"  Merkle Root: {block.merkle_root}")
            print(f"  Nonce: {block.nonce}")
            print(f"  Transactions: {len(block.transactions)}")
            for i, tx in enumerate(block.transactions, 1):
                print(f"    {i}. {tx['from'][:8]}... → {tx['to'][:8]}... : {tx['amount']} coins")


def demonstrate_blockchain():
    """Full blockchain demonstration"""
    
    print("="*70)
    print("BLOCKCHAIN CRYPTOGRAPHY DEMONSTRATION")
    print("="*70)
    
    # Create blockchain
    print("\n[1] INITIALIZING BLOCKCHAIN")
    print("-"*70)
    blockchain = Blockchain(difficulty=4)
    
    # Create wallets
    print("\n[2] CREATING DIGITAL WALLETS")
    print("-"*70)
    alice_wallet = DigitalWallet("Alice")
    bob_wallet = DigitalWallet("Bob")
    charlie_wallet = DigitalWallet("Charlie")
    
    print(f"Alice's address: {alice_wallet.address}")
    print(f"Bob's address: {bob_wallet.address}")
    print(f"Charlie's address: {charlie_wallet.address}")
    
    # Create and sign transactions
    print("\n[3] CREATING SIGNED TRANSACTIONS")
    print("-"*70)
    
    # Give Alice some initial coins (simulate)
    blockchain.mine_pending_transactions(alice_wallet.address)
    
    # Alice sends to Bob
    tx1 = {
        'from': alice_wallet.address,
        'to': bob_wallet.address,
        'amount': 10,
        'timestamp': time.time()
    }
    sig1 = alice_wallet.sign_transaction(tx1)
    blockchain.add_transaction(tx1, sig1, alice_wallet)
    
    # Alice sends to Charlie
    tx2 = {
        'from': alice_wallet.address,
        'to': charlie_wallet.address,
        'amount': 15,
        'timestamp': time.time()
    }
    sig2 = alice_wallet.sign_transaction(tx2)
    blockchain.add_transaction(tx2, sig2, alice_wallet)
    
    # Mine block
    print("\n[4] MINING BLOCK")
    print("-"*70)
    blockchain.mine_pending_transactions(bob_wallet.address)
    
    # Bob sends to Charlie
    tx3 = {
        'from': bob_wallet.address,
        'to': charlie_wallet.address,
        'amount': 5,
        'timestamp': time.time()
    }
    sig3 = bob_wallet.sign_transaction(tx3)
    blockchain.add_transaction(tx3, sig3, bob_wallet)
    
    # Mine another block
    blockchain.mine_pending_transactions(charlie_wallet.address)
    
    # Display blockchain
    blockchain.display_chain()
    
    # Show balances
    print("\n[5] ACCOUNT BALANCES")
    print("-"*70)
    print(f"Alice: {blockchain.get_balance(alice_wallet.address)} coins")
    print(f"Bob: {blockchain.get_balance(bob_wallet.address)} coins")
    print(f"Charlie: {blockchain.get_balance(charlie_wallet.address)} coins")
    
    # Validate chain
    print("\n[6] BLOCKCHAIN VALIDATION")
    print("-"*70)
    blockchain.validate_chain()
    
    # Demonstrate tampering
    blockchain.demonstrate_tampering()
    
    # Merkle tree demonstration
    print("\n[7] MERKLE TREE VERIFICATION")
    print("-"*70)
    block = blockchain.chain[1]
    merkle_tree = block.merkle_tree
    
    print(f"Merkle Root: {merkle_tree.root}")
    print(f"Transactions in block: {len(block.transactions)}")
    
    # Verify a transaction
    tx_index = 0
    tx = json.dumps(block.transactions[tx_index], sort_keys=True)
    proof = merkle_tree.get_proof(tx_index)
    is_valid = merkle_tree.verify_proof(tx, proof, merkle_tree.root)
    
    print(f"\nVerifying transaction {tx_index}:")
    print(f"  Proof length: {len(proof)} hashes")
    print(f"  Valid: {is_valid}")
    
    # Consensus discussion
    print("\n[8] CONSENSUS MECHANISMS")
    print("-"*70)
    consensus_info = """
    PROOF OF WORK (PoW) - Used in Bitcoin
    • Miners compete to solve cryptographic puzzle
    • First to find valid nonce broadcasts block
    • Energy intensive but highly secure
    • Difficulty adjusts based on network hashrate
    
    PROOF OF STAKE (PoS) - Used in Ethereum 2.0
    • Validators stake cryptocurrency to validate blocks
    • Selected based on stake amount and age
    • Energy efficient compared to PoW
    • Risk of "nothing at stake" problem
    
    DELEGATED PROOF OF STAKE (DPoS)
    • Stakeholders vote for delegates
    • Delegates validate transactions
    • Faster but more centralized
    
    PRACTICAL BYZANTINE FAULT TOLERANCE (PBFT)
    • Used in permissioned blockchains
    • Consensus through voting among known validators
    • Fast but requires known participants
    """
    print(consensus_info)
    
    # Public key cryptography in blockchain
    print("\n[9] PUBLIC KEY CRYPTOGRAPHY ROLE")
    print("-"*70)
    crypto_role = """
    In Bitcoin/Ethereum:
    
    1. Wallet Address Generation:
       Private Key → Public Key → Address (via hashing)
       
    2. Transaction Signing:
       • User signs transaction with private key (ECDSA)
       • Network verifies with public key
       • Proves ownership without revealing private key
       
    3. Non-repudiation:
       • Signed transactions cannot be denied
       • Immutable record on blockchain
       
    4. Elliptic Curve Cryptography (ECC):
       • Bitcoin uses secp256k1 curve
       • 256-bit private key
       • Smaller keys than RSA for same security
       
    5. Hash Functions:
       • SHA-256 for Bitcoin
       • Keccak-256 for Ethereum
       • RIPEMD-160 for address generation
    """
    print(crypto_role)


if __name__ == "__main__":
    demonstrate_blockchain()
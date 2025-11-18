"""
Q1: Key Management and Distribution System
Simulates a Key Distribution Center (KDC) for symmetric key distribution
"""

import os
import json
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import base64

class KeyDistributionCenter:
    """Simulates a trusted KDC for symmetric key distribution"""
    
    def __init__(self):
        self.master_keys = {}  # Store master keys for each user
        self.session_keys = {}  # Track active session keys
        self.key_escrow = {}   # Escrowed keys for recovery
        
    def register_user(self, user_id):
        """Register a user and generate their master key"""
        master_key = os.urandom(32)  # 256-bit key
        self.master_keys[user_id] = master_key
        # Key escrow - store encrypted backup
        self.key_escrow[user_id] = {
            'key': base64.b64encode(master_key).decode(),
            'timestamp': time.time(),
            'rotations': 0
        }
        print(f"✓ User '{user_id}' registered with KDC")
        return master_key
    
    def request_session_key(self, user_a, user_b):
        """
        Simulate Needham-Schroeder protocol:
        1. A requests session key for communication with B
        2. KDC generates session key
        3. KDC encrypts session key with A's and B's master keys
        """
        if user_a not in self.master_keys or user_b not in self.master_keys:
            raise ValueError("Both users must be registered")
        
        # Generate session key
        session_key = os.urandom(32)
        session_id = f"{user_a}_{user_b}_{int(time.time())}"
        
        # Encrypt session key for User A
        ticket_a = self._encrypt_ticket(session_key, self.master_keys[user_a], user_b)
        
        # Encrypt session key for User B (ticket)
        ticket_b = self._encrypt_ticket(session_key, self.master_keys[user_b], user_a)
        
        self.session_keys[session_id] = {
            'key': session_key,
            'users': (user_a, user_b),
            'created': time.time()
        }
        
        print(f"✓ Session key generated for {user_a} <-> {user_b}")
        return ticket_a, ticket_b, session_id
    
    def _encrypt_ticket(self, session_key, master_key, peer_id):
        """Encrypt session key with user's master key"""
        iv = os.urandom(16)
        cipher = Cipher(
            algorithms.AES(master_key),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        
        # Pad session key to block size
        padded_key = session_key + b'\x00' * (16 - len(session_key) % 16)
        encrypted = encryptor.update(padded_key) + encryptor.finalize()
        
        return {
            'iv': base64.b64encode(iv).decode(),
            'encrypted_key': base64.b64encode(encrypted).decode(),
            'peer': peer_id
        }
    
    def rotate_key(self, user_id):
        """Simulate key rotation for a user"""
        if user_id not in self.master_keys:
            raise ValueError("User not registered")
        
        old_key = self.master_keys[user_id]
        new_key = os.urandom(32)
        
        # Update master key
        self.master_keys[user_id] = new_key
        
        # Update escrow
        self.key_escrow[user_id]['key'] = base64.b64encode(new_key).decode()
        self.key_escrow[user_id]['rotations'] += 1
        self.key_escrow[user_id]['timestamp'] = time.time()
        
        print(f"✓ Key rotated for user '{user_id}' (rotation #{self.key_escrow[user_id]['rotations']})")
        return new_key


class AsymmetricKeyManager:
    """Manages asymmetric key pairs and distribution"""
    
    def __init__(self):
        self.public_keys = {}
        self.private_keys = {}
    
    def generate_keypair(self, user_id):
        """Generate RSA key pair for a user"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        
        self.private_keys[user_id] = private_key
        self.public_keys[user_id] = public_key
        
        print(f"✓ RSA key pair generated for '{user_id}'")
        return private_key, public_key
    
    def get_public_key(self, user_id):
        """Simulate public key directory lookup"""
        return self.public_keys.get(user_id)
    
    def encrypt_with_public_key(self, message, recipient_id):
        """Encrypt message with recipient's public key"""
        public_key = self.get_public_key(recipient_id)
        if not public_key:
            raise ValueError(f"No public key for {recipient_id}")
        
        encrypted = public_key.encrypt(
            message.encode() if isinstance(message, str) else message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted


def demonstrate_key_distribution():
    """Demonstrate both symmetric and asymmetric key distribution"""
    
    print("=" * 60)
    print("KEY DISTRIBUTION DEMONSTRATION")
    print("=" * 60)
    
    # Symmetric Key Distribution via KDC
    print("\n[1] SYMMETRIC KEY DISTRIBUTION (KDC Model)")
    print("-" * 60)
    kdc = KeyDistributionCenter()
    
    # Register users
    kdc.register_user("Alice")
    kdc.register_user("Bob")
    kdc.register_user("Charlie")
    
    # Request session key
    ticket_a, ticket_b, session_id = kdc.request_session_key("Alice", "Bob")
    print(f"   Session ID: {session_id}")
    
    # Demonstrate key rotation
    print("\n[2] KEY ROTATION")
    print("-" * 60)
    kdc.rotate_key("Alice")
    kdc.rotate_key("Alice")  # Rotate again
    
    # Asymmetric Key Distribution
    print("\n[3] ASYMMETRIC KEY DISTRIBUTION (Public Key Infrastructure)")
    print("-" * 60)
    key_manager = AsymmetricKeyManager()
    
    key_manager.generate_keypair("Alice")
    key_manager.generate_keypair("Bob")
    
    # Demonstrate encryption
    message = "Secret message for Bob"
    encrypted = key_manager.encrypt_with_public_key(message, "Bob")
    print(f"✓ Message encrypted for Bob (length: {len(encrypted)} bytes)")
    
    # Key Escrow Report
    print("\n[4] KEY ESCROW STATUS")
    print("-" * 60)
    for user, escrow_data in kdc.key_escrow.items():
        print(f"User: {user}")
        print(f"  Rotations: {escrow_data['rotations']}")
        print(f"  Last Updated: {time.ctime(escrow_data['timestamp'])}")
    
    # Challenges Discussion
    print("\n[5] CHALLENGES IN LARGE-SCALE ENVIRONMENTS")
    print("-" * 60)
    challenges = {
        "Cloud": [
            "Multi-tenancy key isolation",
            "Geographic key distribution",
            "Compliance with regional regulations (GDPR, etc.)",
            "Key synchronization across data centers"
        ],
        "IoT": [
            "Limited computational resources for key operations",
            "Massive scale (billions of devices)",
            "Secure key storage in constrained devices",
            "Battery-efficient key management protocols"
        ],
        "General": [
            "Key rotation without service disruption",
            "Secure key escrow and recovery mechanisms",
            "Quantum-resistant key exchange migration",
            "Insider threat mitigation"
        ]
    }
    
    for category, items in challenges.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  • {item}")


if __name__ == "__main__":
    demonstrate_key_distribution()
    
    print("\n" + "=" * 60)
    print("COMPARISON: Symmetric vs Asymmetric Key Distribution")
    print("=" * 60)
    
    comparison = """
    ┌─────────────────┬──────────────────────┬──────────────────────┐
    │ Aspect          │ Symmetric            │ Asymmetric           │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Key Exchange    │ Requires secure      │ Public key can be    │
    │                 │ channel (KDC)        │ openly distributed   │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Speed           │ Fast (AES, 3DES)     │ Slow (RSA, ECC)      │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Key Management  │ O(n²) keys needed    │ O(n) keys needed     │
    │                 │ without KDC          │                      │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Use Case        │ Bulk encryption,     │ Key exchange,        │
    │                 │ session keys         │ digital signatures   │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Trust Model     │ Trusted third party  │ PKI/Web of Trust     │
    │                 │ (KDC)                │                      │
    └─────────────────┴──────────────────────┴──────────────────────┘
    """
    print(comparison)
"""
Secure Email Using PGP-like Implementation
Demonstrates Hybrid Encryption (RSA + AES) and Digital Signatures
"""

import os
import base64
from datetime import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.backends import default_backend

class SimplePGPDemo:
    """
    PGP demonstration using pure Python cryptography library.
    Implements 'Hybrid Encryption':
    1. Message encrypted with symmetric key (AES)
    2. Symmetric key encrypted with asymmetric public key (RSA)
    """
    
    def __init__(self):
        self.private_keys = {}
        self.public_keys = {}
    
    def generate_key_pair(self, user_id):
        """Generate RSA key pair for user"""
        print(f"Generating 2048-bit RSA keys for {user_id}...")
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        
        self.private_keys[user_id] = private_key
        self.public_keys[user_id] = public_key
        
        # Save keys to files (simulation)
        self._save_private_key(user_id, private_key)
        self._save_public_key(user_id, public_key)
        
        print(f"✓ Key pair generated for {user_id}")
        return private_key, public_key
    
    def _save_private_key(self, user_id, private_key):
        """Save private key to PEM file"""
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        # Using sanitize filename to prevent errors
        filename = f"{user_id.replace('@','_').replace('.','_')}_private.pem"
        
        # Ensure directory exists
        if not os.path.exists("emails"):
            os.makedirs("emails")
            
        filepath = os.path.join("emails", filename)
        with open(filepath, 'wb') as f:
            f.write(pem)
    
    def _save_public_key(self, user_id, public_key):
        """Save public key to PEM file"""
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        filename = f"{user_id.replace('@','_').replace('.','_')}_public.pem"
        
        # Ensure directory exists
        if not os.path.exists("emails"):
            os.makedirs("emails")
            
        filepath = os.path.join("emails", filename)
        with open(filepath, 'wb') as f:
            f.write(pem)
    
    def encrypt_message(self, message, recipient_id):
        """Encrypt message for recipient using hybrid encryption"""
        if recipient_id not in self.public_keys:
            raise ValueError(f"Public key for {recipient_id} not found!")

        public_key = self.public_keys[recipient_id]
        
        # 1. Generate random AES key (Session Key) and IV
        aes_key = os.urandom(32)  # 256-bit AES key
        iv = os.urandom(16)       # 128-bit IV
        
        # 2. Pad message to AES block size (PKCS7)
        padder = sym_padding.PKCS7(128).padder()
        message_bytes = message.encode('utf-8')
        padded_data = padder.update(message_bytes) + padder.finalize()
        
        # 3. Encrypt message with AES (Symmetric)
        cipher = Cipher(
            algorithms.AES(aes_key),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
        
        # 4. Encrypt AES key with recipient's public key (Asymmetric/RSA)
        encrypted_key = public_key.encrypt(
            aes_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # 5. Combine: [Encrypted AES Key (256 bytes)] + [IV (16 bytes)] + [Encrypted Message]
        combined = encrypted_key + iv + encrypted_message
        encrypted_b64 = base64.b64encode(combined).decode('utf-8')
        
        print(f"✓ Message encrypted for {recipient_id} (Size: {len(encrypted_b64)} bytes)")
        return encrypted_b64
    
    def decrypt_message(self, encrypted_message_b64, recipient_id):
        """Decrypt message using hybrid decryption"""
        if recipient_id not in self.private_keys:
            raise ValueError(f"Private key for {recipient_id} not found!")

        private_key = self.private_keys[recipient_id]
        
        try:
            combined = base64.b64decode(encrypted_message_b64)
            
            # Extract parts (Assuming 2048-bit RSA key = 256 bytes encrypted key)
            encrypted_key_len = 256
            iv_len = 16
            
            encrypted_key = combined[:encrypted_key_len]
            iv = combined[encrypted_key_len : encrypted_key_len + iv_len]
            encrypted_message = combined[encrypted_key_len + iv_len:]
            
            # 1. Decrypt AES key with recipient's private key (RSA)
            aes_key = private_key.decrypt(
                encrypted_key,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            
            # 2. Decrypt message with AES
            cipher = Cipher(
                algorithms.AES(aes_key),
                modes.CBC(iv),
                backend=default_backend()
            )
            decryptor = cipher.decryptor()
            padded_message = decryptor.update(encrypted_message) + decryptor.finalize()
            
            # 3. Remove PKCS7 padding
            unpadder = sym_padding.PKCS7(128).unpadder()
            decrypted_message_bytes = unpadder.update(padded_message) + unpadder.finalize()
            
            print(f"✓ Message decrypted by {recipient_id}")
            return decrypted_message_bytes.decode('utf-8')
            
        except Exception as e:
            print(f"Error decrypting: {e}")
            return None
    
    def sign_message(self, message, sender_id):
        """Create digital signature"""
        private_key = self.private_keys[sender_id]
        
        signature = private_key.sign(
            message.encode('utf-8'),
            asym_padding.PSS(
                mgf=asym_padding.MGF1(hashes.SHA256()),
                salt_length=asym_padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        signature_b64 = base64.b64encode(signature).decode('utf-8')
        print(f"✓ Message signed by {sender_id}")
        return signature_b64
    
    def verify_signature(self, message, signature_b64, sender_id):
        """Verify digital signature"""
        public_key = self.public_keys[sender_id]
        signature = base64.b64decode(signature_b64)
        
        try:
            public_key.verify(
                signature,
                message.encode('utf-8'),
                asym_padding.PSS(
                    mgf=asym_padding.MGF1(hashes.SHA256()),
                    salt_length=asym_padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print(f"✓ Signature verified from {sender_id}")
            return True
        except Exception as e:
            print(f"✗ Signature verification failed: {e}")
            return False
    
    def create_signed_email(self, message, sender_id, recipient_id):
        """Create encrypted and signed email"""
        # 1. Sign the cleartext message
        signature = self.sign_message(message, sender_id)
        
        # 2. Combine message and signature
        # In real PGP, this is more complex (compression, packets), 
        # but for this demo, we append the signature.
        signed_payload = f"{message}\n\n---SIGNATURE---\n{signature}"
        
        # 3. Encrypt the combined payload for the recipient
        encrypted = self.encrypt_message(signed_payload, recipient_id)
        
        return encrypted
    
    def read_signed_email(self, encrypted_email, recipient_id, sender_id):
        """Decrypt and verify signed email"""
        # 1. Decrypt
        decrypted_payload = self.decrypt_message(encrypted_email, recipient_id)
        
        if not decrypted_payload:
            return None
        
        # 2. Split message and signature
        separator = "\n\n---SIGNATURE---\n"
        if separator not in decrypted_payload:
            print("✗ Invalid email format: Signature block missing")
            return {'message': decrypted_payload, 'verified': False, 'sender': 'Unknown'}
            
        message, signature = decrypted_payload.split(separator)
        
        # 3. Verify signature using the extracted message content
        verified = self.verify_signature(message, signature, sender_id)
        
        return {
            'message': message,
            'verified': verified,
            'sender': sender_id
        }


def demonstrate_pgp():
    """Demonstrate PGP email encryption and signing"""
    
    print("=" * 70)
    print("PGP EMAIL DEMONSTRATION")
    print("=" * 70)
    
    pgp = SimplePGPDemo()
    
    # Ensure emails directory exists
    if not os.path.exists("emails"):
        os.makedirs("emails")
    
    # Generate key pairs
    print("\n[1] KEY GENERATION")
    print("-" * 70)
    pgp.generate_key_pair("alice@example.com")
    pgp.generate_key_pair("bob@example.com")
    
    # Create email message
    print("\n[2] COMPOSING EMAIL")
    print("-" * 70)
    email_message = """From: alice@example.com
To: bob@example.com
Subject: Confidential Project Update
Date: {}

Dear Bob,

This is a confidential message about our secret project.
The launch is scheduled for next month.

Best regards,
Alice""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    print(email_message)
    
    # Create signed and encrypted email
    print("\n[3] SIGNING AND ENCRYPTING")
    print("-" * 70)
    encrypted_email = pgp.create_signed_email(
        email_message,
        "alice@example.com",
        "bob@example.com"
    )
    
    # Save encrypted email
    file_path = os.path.join("emails", "signed_email.asc")
    with open(file_path, "w") as f:
        f.write("-----BEGIN PGP MESSAGE-----\n\n")
        f.write(encrypted_email)
        f.write("\n-----END PGP MESSAGE-----\n")
    
    print(f" Encrypted email saved to: {file_path}")
    
    # Bob receives and decrypts
    print("\n[4] DECRYPTING AND VERIFYING")
    print("-" * 70)
    
    # Simulating reading from file
    with open(file_path, "r") as f:
        content = f.read()
        # simplistic parsing for demo
        lines = content.strip().split('\n')
        # Removing header/footer roughly
        clean_encrypted = lines[2] if len(lines) > 3 else encrypted_email 
    
    result = pgp.read_signed_email(
        encrypted_email, # Passing the raw base64 string
        "bob@example.com",
        "alice@example.com"
    )
    
    if result and result['verified']:
        print("\n✓ Email successfully decrypted and verified!")
        print("\nDecrypted message:")
        print("-" * 70)
        print(result['message'])
    else:
        print("\n✗ Failed to decrypt or verify.")

    # Comparison
    print("\n" + "=" * 70)
    print("S/MIME vs PGP COMPARISON")
    print("=" * 70)
    
    comparison = """
    ┌──────────────────┬────────────────────────┬────────────────────────┐
    │ Feature          │ S/MIME                 │ PGP                    │
    ├──────────────────┼────────────────────────┼────────────────────────┤
    │ Trust Model      │ Hierarchical PKI       │ Web of Trust           │
    │                  │ (Certificate Authority)│ (Decentralized)        │
    ├──────────────────┼────────────────────────┼────────────────────────┤
    │ Key Distribution │ X.509 certificates     │ Public keyservers      │
    │                  │ from trusted CAs       │ (keys.openpgp.org)     │
    ├──────────────────┼────────────────────────┼────────────────────────┤
    │ Integration      │ Built into email       │ Requires plugins       │
    │                  │ clients (Outlook, iOS) │ (Thunderbird, Mailvelo)│
    ├──────────────────┼────────────────────────┼────────────────────────┤
    │ Cost             │ Requires paid CA cert  │ Free and open source   │
    ├──────────────────┼────────────────────────┼────────────────────────┤
    │ Revocation       │ CRL and OCSP           │ Key revocation certs   │
    ├──────────────────┼────────────────────────┼────────────────────────┤
    │ Standards        │ IETF RFC 8551          │ OpenPGP RFC 4880       │
    ├──────────────────┼────────────────────────┼────────────────────────┤
    │ Best For         │ Corporate email        │ Privacy-focused users  │
    │                  │ Enterprise use         │ Personal communication │
    └──────────────────┴────────────────────────┴────────────────────────┘
    """
    print(comparison)

if __name__ == "__main__":
    demonstrate_pgp()
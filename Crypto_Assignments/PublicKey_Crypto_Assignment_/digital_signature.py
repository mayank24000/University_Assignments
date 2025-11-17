#!/usr/bin/env python3
"""
Q2: Digital Signatures using RSA/DSA
"""

from Crypto.PublicKey import RSA, DSA
from Crypto.Signature import pkcs1_15, DSS
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import time

# Colorama is optional - use fallback if not available
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    # Fallback class when colorama is not installed
    class Fore:
        CYAN = YELLOW = GREEN = RED = MAGENTA = ''
    class Style:
        BRIGHT = ''

class DigitalSignature:
    """Digital Signature Implementation using RSA and DSA"""
    
    def __init__(self):
        self.rsa_key = None
        self.dsa_key = None
        
    def generate_rsa_keypair(self, keysize=2048):
        """Generate RSA key pair for signatures"""
        print(f"{Fore.CYAN}Generating {keysize}-bit RSA key pair for signatures...")
        start = time.time()
        self.rsa_key = RSA.generate(keysize)
        end = time.time()
        print(f"{Fore.GREEN}✓ RSA keys generated in {end-start:.4f} seconds")
        
        # Save keys
        with open('rsa_signing_key.pem', 'wb') as f:
            f.write(self.rsa_key.export_key())
        with open('rsa_verify_key.pem', 'wb') as f:
            f.write(self.rsa_key.publickey().export_key())
            
        return self.rsa_key
    
    def generate_dsa_keypair(self, keysize=2048):
        """Generate DSA key pair for signatures"""
        print(f"{Fore.CYAN}Generating {keysize}-bit DSA key pair for signatures...")
        start = time.time()
        self.dsa_key = DSA.generate(keysize)
        end = time.time()
        print(f"{Fore.GREEN}✓ DSA keys generated in {end-start:.4f} seconds")
        
        # Save keys
        with open('dsa_signing_key.pem', 'wb') as f:
            f.write(self.dsa_key.export_key())
        with open('dsa_verify_key.pem', 'wb') as f:
            f.write(self.dsa_key.publickey().export_key())
            
        return self.dsa_key
    
    def sign_message_rsa(self, message):
        """Sign a message using RSA"""
        if not self.rsa_key:
            self.generate_rsa_keypair()
            
        # Hash the message
        h = SHA256.new(message)
        
        # Sign the hash
        signature = pkcs1_15.new(self.rsa_key).sign(h)
        
        print(f"{Fore.GREEN}✓ Message signed with RSA")
        print(f"{Fore.YELLOW}Signature (hex): {signature.hex()[:80]}...")
        
        return signature, h
    
    def verify_signature_rsa(self, message, signature, public_key=None):
        """Verify RSA signature"""
        if public_key is None:
            public_key = self.rsa_key.publickey()
            
        h = SHA256.new(message)
        
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            print(f"{Fore.GREEN}✓ RSA Signature verified successfully!")
            return True
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}✗ RSA Signature verification failed: {e}")
            return False
    
    def sign_message_dsa(self, message):
        """Sign a message using DSA"""
        if not self.dsa_key:
            self.generate_dsa_keypair()
            
        # Hash the message
        h = SHA256.new(message)
        
        # Sign the hash
        signature = DSS.new(self.dsa_key, 'fips-186-3').sign(h)
        
        print(f"{Fore.GREEN}✓ Message signed with DSA")
        print(f"{Fore.YELLOW}Signature (hex): {signature.hex()[:80]}...")
        
        return signature, h
    
    def verify_signature_dsa(self, message, signature, public_key=None):
        """Verify DSA signature"""
        if public_key is None:
            public_key = self.dsa_key.publickey()
            
        h = SHA256.new(message)
        
        try:
            DSS.new(public_key, 'fips-186-3').verify(h, signature)
            print(f"{Fore.GREEN}✓ DSA Signature verified successfully!")
            return True
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}✗ DSA Signature verification failed: {e}")
            return False
    
    def demonstrate_tampering(self, message, signature, algorithm='RSA'):
        """Demonstrate what happens when message is tampered"""
        print(f"\n{Fore.YELLOW}=== Demonstrating Message Tampering ===")
        
        # Tamper with the message
        tampered_message = message.replace(b"secure", b"hacked")
        print(f"Original: {message.decode()}")
        print(f"Tampered: {tampered_message.decode()}")
        
        if algorithm == 'RSA':
            result = self.verify_signature_rsa(tampered_message, signature)
        else:
            result = self.verify_signature_dsa(tampered_message, signature)
            
        if not result:
            print(f"{Fore.GREEN}✓ Tampering detected! Signature verification failed as expected.")

def explain_digital_signatures():
    """Explain how digital signatures ensure authenticity and non-repudiation"""
    print(f"\n{Fore.CYAN}=== Digital Signatures: Authenticity & Non-Repudiation ===")
    print(f"""
{Fore.YELLOW}1. AUTHENTICITY:
   • Signature can only be created with private key
   • Public key verifies sender's identity
   • Prevents impersonation attacks
   
{Fore.YELLOW}2. INTEGRITY:
   • Any change to message invalidates signature
   • Hash function ensures message hasn't been altered
   • Detects tampering attempts
   
{Fore.YELLOW}3. NON-REPUDIATION:
   • Signer cannot deny signing the message
   • Private key uniquely identifies the signer
   • Provides legal proof of origin
   
{Fore.GREEN}Process:
   1. Sender hashes the message
   2. Encrypts hash with private key (signature)
   3. Sends message + signature
   4. Receiver hashes the message
   5. Decrypts signature with public key
   6. Compares hashes - if match, signature valid!
    """)

def main():
    print(f"{Style.BRIGHT}{Fore.MAGENTA}=== Q2: Digital Signatures ===\n")
    
    if not HAS_COLOR:
        print("Note: Install 'colorama' for colored output: pip install colorama\n")
    
    ds = DigitalSignature()
    
    # Test message
    message = b"This is a secure and authenticated message"
    
    # RSA Signatures
    print(f"{Fore.CYAN}Part A: RSA Digital Signatures")
    print("="*50)
    ds.generate_rsa_keypair()
    print(f"\n{Fore.YELLOW}Message to sign: {message.decode()}")
    
    # Sign and verify with RSA
    rsa_signature, _ = ds.sign_message_rsa(message)
    ds.verify_signature_rsa(message, rsa_signature)
    
    # Demonstrate tampering detection
    ds.demonstrate_tampering(message, rsa_signature, 'RSA')
    
    # DSA Signatures
    print(f"\n{Fore.CYAN}Part B: DSA Digital Signatures")
    print("="*50)
    ds.generate_dsa_keypair()
    
    # Sign and verify with DSA
    dsa_signature, _ = ds.sign_message_dsa(message)
    ds.verify_signature_dsa(message, dsa_signature)
    
    # Demonstrate tampering detection
    ds.demonstrate_tampering(message, dsa_signature, 'DSA')
    
    # Explain concepts
    print(f"\n{Fore.CYAN}Part C: Discussion")
    print("="*50)
    explain_digital_signatures()
    
    print(f"\n{Fore.GREEN}✓ Q2 Complete! Check generated signature key files.")

if __name__ == "__main__":
    main()
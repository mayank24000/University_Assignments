#!/usr/bin/env python3
"""
Q1: RSA Encryption/Decryption and Diffie-Hellman Key Exchange
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

class RSADemo:
    """RSA Encryption and Decryption Implementation"""
    
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.private_key = None
        self.public_key = None
        
    def generate_keys(self):
        """Generate RSA key pair"""
        print(f"{Fore.CYAN}Generating {self.key_size}-bit RSA key pair...")
        start = time.time()
        key = RSA.generate(self.key_size)
        self.private_key = key
        self.public_key = key.publickey()
        end = time.time()
        print(f"{Fore.GREEN}✓ Keys generated in {end-start:.4f} seconds")
        
        # Export keys
        private_pem = key.export_key()
        public_pem = self.public_key.export_key()
        
        # Save keys to files
        with open('private_key.pem', 'wb') as f:
            f.write(private_pem)
        with open('public_key.pem', 'wb') as f:
            f.write(public_pem)
            
        print(f"{Fore.YELLOW}Keys saved to private_key.pem and public_key.pem")
        
        return public_pem, private_pem
    
    def encrypt(self, message, public_key=None):
        """Encrypt message using RSA"""
        if public_key is None:
            public_key = self.public_key
            
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(message)
        return ciphertext
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using RSA"""
        cipher = PKCS1_OAEP.new(self.private_key)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext

class DiffieHellman:
    """Diffie-Hellman Key Exchange Implementation"""
    
    def __init__(self):
        # Large prime and generator for production use
        self.p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
        self.g = 2
        
    def generate_private_key(self):
        """Generate private key for DH"""
        return random.randint(2, self.p - 2)
    
    def generate_public_key(self, private_key):
        """Generate public key from private key"""
        return pow(self.g, private_key, self.p)
    
    def compute_shared_secret(self, other_public, my_private):
        """Compute shared secret"""
        return pow(other_public, my_private, self.p)
    
    def simulate_exchange(self):
        """Simulate complete DH key exchange between Alice and Bob"""
        print(f"\n{Fore.CYAN}=== Diffie-Hellman Key Exchange Simulation ===")
        
        # Alice generates keys
        print(f"{Fore.YELLOW}Alice generating keys...")
        alice_private = self.generate_private_key()
        alice_public = self.generate_public_key(alice_private)
        print(f"Alice's public key: {hex(alice_public)[:50]}...")
        
        # Bob generates keys
        print(f"\n{Fore.YELLOW}Bob generating keys...")
        bob_private = self.generate_private_key()
        bob_public = self.generate_public_key(bob_private)
        print(f"Bob's public key: {hex(bob_public)[:50]}...")
        
        # Exchange and compute shared secrets
        print(f"\n{Fore.CYAN}Computing shared secrets...")
        alice_shared = self.compute_shared_secret(bob_public, alice_private)
        bob_shared = self.compute_shared_secret(alice_public, bob_private)
        
        print(f"{Fore.GREEN}✓ Alice's shared secret: {hex(alice_shared)[:50]}...")
        print(f"{Fore.GREEN}✓ Bob's shared secret: {hex(bob_shared)[:50]}...")
        
        if alice_shared == bob_shared:
            print(f"\n{Fore.GREEN}✓ SUCCESS! Shared secrets match!")
        else:
            print(f"\n{Fore.RED}✗ ERROR! Shared secrets don't match!")
            
        return alice_shared

def compare_rsa_dh():
    """Compare RSA and Diffie-Hellman"""
    print(f"\n{Fore.CYAN}=== RSA vs Diffie-Hellman Comparison ===")
    print(f"""
{Fore.YELLOW}RSA:
• Type: Asymmetric encryption & digital signatures
• Key Size: 2048-4096 bits typically
• Use Cases: Encryption, digital signatures, key transport
• Speed: Slower for encryption/decryption
• Security: Based on factoring large primes

{Fore.YELLOW}Diffie-Hellman:
• Type: Key exchange protocol only
• Key Size: 2048-4096 bits for modulus
• Use Cases: Secure key exchange
• Speed: Faster than RSA encryption
• Security: Based on discrete logarithm problem

{Fore.GREEN}Key Differences:
1. RSA can encrypt data directly; DH only exchanges keys
2. RSA supports digital signatures; DH does not
3. DH is more efficient for key exchange
4. Both vulnerable to quantum computing
5. Often used together in protocols like TLS
    """)

def main():
    print(f"{Style.BRIGHT}{Fore.MAGENTA}=== Q1: Public Key Encryption & Key Exchange ===\n")
    
    # RSA Demo
    print(f"{Fore.CYAN}Part A: RSA Encryption/Decryption")
    print("="*50)
    rsa_demo = RSADemo(2048)
    rsa_demo.generate_keys()
    
    # Encrypt and decrypt a message
    message = b"This is a secure message using RSA encryption!"
    print(f"\n{Fore.YELLOW}Original message: {message.decode()}")
    
    ciphertext = rsa_demo.encrypt(message)
    print(f"{Fore.YELLOW}Ciphertext (hex): {ciphertext.hex()[:80]}...")
    
    decrypted = rsa_demo.decrypt(ciphertext)
    print(f"{Fore.GREEN}✓ Decrypted message: {decrypted.decode()}")
    
    # Diffie-Hellman Demo
    print(f"\n{Fore.CYAN}Part B: Diffie-Hellman Key Exchange")
    print("="*50)
    dh = DiffieHellman()
    shared_secret = dh.simulate_exchange()
    
    # Comparison
    print(f"\n{Fore.CYAN}Part C: Comparison")
    print("="*50)
    compare_rsa_dh()
    
    print(f"\n{Fore.GREEN}✓ Q1 Complete! Check generated key files.")

if __name__ == "__main__":
    main()
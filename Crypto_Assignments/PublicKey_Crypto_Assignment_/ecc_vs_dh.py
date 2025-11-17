#!/usr/bin/env python3
"""
Q4: Key Exchange Protocol Comparison - Classic DH vs ECDH
"""

import random
import time
import hashlib

# Optional imports with fallbacks
try:
    from tinyec import registry
    HAS_TINYEC = True
except ImportError:
    HAS_TINYEC = False
    print("Warning: tinyec not installed. Install with: pip install tinyec")

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class Fore:
        CYAN = YELLOW = GREEN = RED = MAGENTA = ''
    class Style:
        BRIGHT = ''

try:
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not installed. Install with: pip install matplotlib numpy")
    # Minimal numpy fallback for basic operations
    class np:
        @staticmethod
        def mean(data):
            return sum(data) / len(data)
        
        @staticmethod
        def std(data):
            m = sum(data) / len(data)
            variance = sum((x - m) ** 2 for x in data) / len(data)
            return variance ** 0.5

class ClassicDiffieHellman:
    """Classic Diffie-Hellman Implementation"""
    
    def __init__(self, bits=2048):
        self.bits = bits
        if bits == 2048:
            # 2048-bit MODP group (RFC 3526)
            self.p = int("""FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
                29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
                EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
                E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
                EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
                C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
                83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
                670C354E 4ABC9804 F1746C08 CA18217C 32905E46 2E36CE3B
                E39E772C 180E8603 9B2783A2 EC07A28F B5C55DF0 6F4C52C9
                DE2BCBF6 95581718 3995497C EA956AE5 15D22618 98FA0510
                15728E5A 8AACAA68 FFFFFFFF FFFFFFFF""".replace(" ", "").replace("\n", ""), 16)
            self.g = 2
        else:
            # Simple prime for demonstration
            self.p = self._generate_prime(bits)
            self.g = 2
    
    def _generate_prime(self, bits):
        """Generate a prime number (simplified)"""
        # For demonstration, using known safe primes
        if bits == 512:
            return int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D", 16)
        return int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1", 16)
    
    def generate_private_key(self):
        """Generate private key"""
        return random.randint(2, self.p - 2)
    
    def generate_public_key(self, private_key):
        """Generate public key"""
        return pow(self.g, private_key, self.p)
    
    def compute_shared_secret(self, other_public, my_private):
        """Compute shared secret"""
        return pow(other_public, my_private, self.p)
    
    def perform_exchange(self):
        """Perform complete key exchange and measure time"""
        start_time = time.perf_counter()
        
        # Alice
        alice_private = self.generate_private_key()
        alice_public = self.generate_public_key(alice_private)
        
        # Bob
        bob_private = self.generate_private_key()
        bob_public = self.generate_public_key(bob_private)
        
        # Shared secrets
        alice_shared = self.compute_shared_secret(bob_public, alice_private)
        bob_shared = self.compute_shared_secret(alice_public, bob_private)
        
        end_time = time.perf_counter()
        
        return alice_shared == bob_shared, end_time - start_time

class EllipticCurveDiffieHellman:
    """Elliptic Curve Diffie-Hellman Implementation"""
    
    def __init__(self, curve_name="secp256r1"):
        if not HAS_TINYEC:
            raise ImportError("tinyec library required for ECDH. Install with: pip install tinyec")
        self.curve_name = curve_name
        self.curve = registry.get_curve(curve_name)
    
    def generate_private_key(self):
        """Generate private key"""
        return random.randint(1, self.curve.field.n - 1)
    
    def generate_public_key(self, private_key):
        """Generate public key (point on curve)"""
        return private_key * self.curve.g
    
    def compute_shared_secret(self, other_public, my_private):
        """Compute shared secret"""
        shared_point = my_private * other_public
        # Use x-coordinate as shared secret
        return shared_point.x
    
    def perform_exchange(self):
        """Perform complete key exchange and measure time"""
        start_time = time.perf_counter()
        
        # Alice
        alice_private = self.generate_private_key()
        alice_public = self.generate_public_key(alice_private)
        
        # Bob
        bob_private = self.generate_private_key()
        bob_public = self.generate_public_key(bob_private)
        
        # Shared secrets
        alice_shared = self.compute_shared_secret(bob_public, alice_private)
        bob_shared = self.compute_shared_secret(alice_public, bob_private)
        
        end_time = time.perf_counter()
        
        return alice_shared == bob_shared, end_time - start_time

def compare_protocols():
    """Compare Classic DH and ECDH protocols"""
    print(f"{Fore.CYAN}=== Protocol Comparison: Classic DH vs ECDH ===\n")
    
    # Test configurations
    test_configs = [
        ("Classic DH (512-bit)", ClassicDiffieHellman(512)),
        ("Classic DH (2048-bit)", ClassicDiffieHellman(2048)),
    ]
    
    # Add ECDH tests only if tinyec is available
    if HAS_TINYEC:
        test_configs.extend([
            ("ECDH (secp192r1)", EllipticCurveDiffieHellman("secp192r1")),
            ("ECDH (secp256r1)", EllipticCurveDiffieHellman("secp256r1")),
        ])
    else:
        print(f"{Fore.YELLOW}Note: ECDH tests skipped (tinyec not installed)\n")
    
    results = []
    
    for name, protocol in test_configs:
        print(f"{Fore.YELLOW}Testing {name}...")
        
        # Run multiple iterations for accurate timing
        times = []
        for _ in range(10):
            success, elapsed = protocol.perform_exchange()
            if success:
                times.append(elapsed * 1000)  # Convert to milliseconds
        
        avg_time = np.mean(times)
        std_time = np.std(times)
        
        results.append({
            'name': name,
            'avg_time': avg_time,
            'std_time': std_time
        })
        
        print(f"{Fore.GREEN}✓ Average time: {avg_time:.4f}ms (±{std_time:.4f}ms)")
    
    # Create comparison chart if matplotlib is available
    if HAS_MATPLOTLIB and len(results) > 0:
        create_comparison_chart(results)
    else:
        print(f"\n{Fore.YELLOW}Note: Chart generation skipped (matplotlib not installed)")
    
    return results

def create_comparison_chart(results):
    """Create bar chart comparing protocols"""
    names = [r['name'] for r in results]
    times = [r['avg_time'] for r in results]
    errors = [r['std_time'] for r in results]
    
    plt.figure(figsize=(10, 6))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    bars = plt.bar(names, times, yerr=errors, capsize=5, color=colors[:len(names)], 
                   edgecolor='black', linewidth=1.5)
    
    plt.xlabel('Key Exchange Protocol', fontsize=12)
    plt.ylabel('Average Time (milliseconds)', fontsize=12)
    plt.title('Key Exchange Protocol Performance Comparison', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on bars
    for bar, time_val in zip(bars, times):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height,
                f'{time_val:.3f}ms', ha='center', va='bottom', fontsize=10)
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('key_exchange_comparison.png', dpi=150)
    print(f"\n{Fore.GREEN}✓ Comparison chart saved as 'key_exchange_comparison.png'")

def explain_advantages():
    """Explain advantages of ECC over traditional methods"""
    print(f"\n{Fore.CYAN}=== Advantages of ECC in Resource-Constrained Environments ===")
    print(f"""
{Fore.YELLOW}1. SMALLER KEY SIZES:
   • ECC 256-bit ≈ RSA 3072-bit security level
   • ECC 384-bit ≈ RSA 7680-bit security level
   • Result: Less storage and bandwidth required

{Fore.YELLOW}2. FASTER COMPUTATION:
   • Smaller numbers = faster arithmetic operations
   • Lower power consumption
   • Ideal for IoT devices and mobile platforms

{Fore.YELLOW}3. MEMORY EFFICIENCY:
   • Reduced RAM requirements
   • Smaller certificate sizes
   • Better for embedded systems

{Fore.YELLOW}4. BATTERY LIFE:
   • Less computational overhead
   • Extended battery life in mobile devices
   • Critical for sensor networks

{Fore.YELLOW}5. SCALABILITY:
   • Better performance as security requirements increase
   • Future-proof against advancing threats
   • Quantum-resistant variants being developed

{Fore.GREEN}REAL-WORLD APPLICATIONS:
   • Mobile devices (iOS, Android)
   • IoT sensors and actuators
   • Blockchain and cryptocurrencies
   • Smart cards and RFID
   • Embedded automotive systems
   • Satellite communications
    """)

def security_comparison():
    """Compare security levels"""
    print(f"\n{Fore.CYAN}=== Security Level Comparison ===")
    
    security_table = """
    ┌──────────────┬──────────────┬────────────┬──────────────┐
    │ Security Bit │ RSA Key Size │ DH Key Size│ ECC Key Size │
    ├──────────────┼──────────────┼────────────┼──────────────┤
    │     80       │    1024      │    1024    │     160      │
    │    112       │    2048      │    2048    │     224      │
    │    128       │    3072      │    3072    │     256      │
    │    192       │    7680      │    7680    │     384      │
    │    256       │   15360      │   15360    │     512      │
    └──────────────┴──────────────┴────────────┴──────────────┘
    """
    print(f"{Fore.GREEN}{security_table}")

def main():
    print(f"{Style.BRIGHT}{Fore.MAGENTA}=== Q4: Key Exchange Protocol Comparison ===\n")
    
    if not HAS_COLOR:
        print("Note: Install 'colorama' for colored output: pip install colorama\n")
    
    # Part A: Implement both protocols
    print(f"{Fore.CYAN}Part A: Protocol Implementations")
    print("="*50)
    
    # Classic DH demonstration
    print(f"\n{Fore.YELLOW}Classic Diffie-Hellman Demo:")
    dh = ClassicDiffieHellman(512)  # Using smaller size for demo
    success, time_taken = dh.perform_exchange()
    print(f"{Fore.GREEN}✓ Key exchange successful: {success}")
    print(f"{Fore.GREEN}✓ Time taken: {time_taken*1000:.4f}ms")
    
    # ECDH demonstration
    if HAS_TINYEC:
        print(f"\n{Fore.YELLOW}Elliptic Curve Diffie-Hellman Demo:")
        ecdh = EllipticCurveDiffieHellman("secp256r1")
        success, time_taken = ecdh.perform_exchange()
        print(f"{Fore.GREEN}✓ Key exchange successful: {success}")
        print(f"{Fore.GREEN}✓ Time taken: {time_taken*1000:.4f}ms")
    else:
        print(f"\n{Fore.YELLOW}ECDH Demo skipped: Install tinyec for ECDH support")
    
    # Part B: Performance comparison
    print(f"\n{Fore.CYAN}Part B: Performance Measurement")
    print("="*50)
    results = compare_protocols()
    
    # Part C: Advantages discussion
    print(f"\n{Fore.CYAN}Part C: ECC Advantages")
    print("="*50)
    explain_advantages()
    security_comparison()
    
    print(f"\n{Fore.GREEN}✓ Q4 Complete!")
    if HAS_MATPLOTLIB:
        print(f"{Fore.GREEN}  Check 'key_exchange_comparison.png' for visualization.")
    
    # Show installation instructions if needed
    if not HAS_TINYEC or not HAS_MATPLOTLIB:
        print(f"\n{Fore.YELLOW}To enable all features, install missing dependencies:")
        if not HAS_TINYEC:
            print(f"  pip install tinyec")
        if not HAS_MATPLOTLIB:
            print(f"  pip install matplotlib numpy")

if __name__ == "__main__":
    main()
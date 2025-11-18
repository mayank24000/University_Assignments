# Q5: Post-Quantum Cryptography - Emerging Trends

## Executive Summary

Quantum computers pose an existential threat to current public-key cryptography systems (RSA, ECC, Diffie-Hellman). This document explores post-quantum cryptographic algorithms, NIST standardization efforts, and the transition roadmap.

---

## 1. The Quantum Threat

### Vulnerable Algorithms

| Algorithm | Key Size | Quantum Attack | Time to Break (Classical) | Time to Break (Quantum) |
|-----------|----------|----------------|---------------------------|-------------------------|
| RSA-2048 | 2048 bits | Shor's Algorithm | 1000+ years | Hours |
| ECC-256 | 256 bits | Shor's Algorithm | Infeasible | Minutes |
| AES-128 | 128 bits | Grover's Algorithm | 2^128 ops | 2^64 ops |
| SHA-256 | 256 bits | Grover's Algorithm | 2^256 ops | 2^128 ops |

### Shor's Algorithm
- Efficiently factors large numbers
- Solves discrete logarithm problem
- **Breaks RSA, DSA, ECDSA, Diffie-Hellman**

### Grover's Algorithm
- Quadratic speedup for search problems
- Reduces AES-128 security to AES-64 equivalent
- **Mitigation**: Double key sizes (AES-256, SHA-512)

---

## 2. NIST Post-Quantum Standardization

### Timeline
2016 - NIST announces PQC competition
2017 - 69 candidates submitted
2019 - 26 algorithms advance to Round 2
2020 - 7 finalists selected for Round 3
2022 - 4 algorithms selected for standardization
2024 - Standards publication (expected)
### Selected Algorithms (2022)

#### 1. **CRYSTALS-Kyber** (Key Encapsulation)
- **Category**: Lattice-based (Module-LWE)
- **Use Case**: Key exchange (replaces ECDH)
- **Key Sizes**:
  - Kyber-512: 800 bytes public key, 1632 bytes ciphertext
  - Kyber-768: 1184 bytes public key, 2400 bytes ciphertext
  - Kyber-1024: 1568 bytes public key, 3168 bytes ciphertext
- **Security**: NIST Levels 1, 3, 5
- **Performance**: Fast encryption/decryption

#### 2. **CRYSTALS-Dilithium** (Digital Signatures)
- **Category**: Lattice-based (Module-LWE/Module-SIS)
- **Use Case**: Digital signatures (replaces RSA, ECDSA)
- **Key Sizes**:
  - Dilithium2: 1312 bytes public key, 2420 bytes signature
  - Dilithium3: 1952 bytes public key, 3293 bytes signature
  - Dilithium5: 2592 bytes public key, 4595 bytes signature
- **Security**: NIST Levels 2, 3, 5

#### 3. **FALCON** (Digital Signatures)
- **Category**: Lattice-based (NTRU)
- **Use Case**: Signatures with smaller size
- **Key Sizes**:
  - FALCON-512: 897 bytes public key, 666 bytes signature
  - FALCON-1024: 1793 bytes public key, 1280 bytes signature
- **Advantage**: Smallest signature size
- **Challenge**: Complex implementation

#### 4. **SPHINCS+** (Digital Signatures)
- **Category**: Hash-based
- **Use Case**: Stateless signatures
- **Key Sizes**: 32-64 bytes public key, 8-49 KB signatures
- **Advantage**: Only relies on hash function security
- **Disadvantage**: Large signature sizes

### Alternate Candidates (Round 4)

- **BIKE**: Code-based KEM
- **Classic McEliece**: Code-based KEM (conservative)
- **HQC**: Code-based KEM
- **SIKE**: Isogeny-based KEM (broken in 2022)

---

## 3. Lattice-Based Cryptography (Detailed)

### Mathematical Foundation

**Learning With Errors (LWE) Problem**:

Given pairs `(aᵢ, bᵢ = <aᵢ, s> + eᵢ mod q)` where:
- `aᵢ` is a random vector
- `s` is a secret vector
- `eᵢ` is a small error
- `q` is a modulus

**Challenge**: Recover secret `s`

### CRYSTALS-Kyber Example (Simplified)

#### Key Generation
```python
# Conceptual implementation
import numpy as np

def kyber_keygen(n=256, q=3329, k=2):
    """
    Simplified Kyber key generation
    n: polynomial degree
    q: modulus
    k: security parameter
    """
    # Generate secret key: small polynomial coefficients
    s = np.random.randint(-2, 3, size=(k, n))  # Small values
    
    # Generate error
    e = np.random.randint(-2, 3, size=(k, n))
    
    # Generate random matrix A
    A = np.random.randint(0, q, size=(k, k, n))
    
    # Public key: pk = A·s + e (mod q)
    pk = (np.tensordot(A, s, axes=([1],[0])) + e) % q
    
    return (pk, A), s  # Public key, Secret key

def kyber_encrypt(pk, message, q=3329):
    """Encrypt a message"""
    pk_vector, A = pk
    
    # Random small vector
    r = np.random.randint(-2, 3, size=pk_vector.shape)
    
    # Encrypt
    u = (np.tensordot(A.transpose(1,0,2), r, axes=([1],[0]))) % q
    v = (np.dot(pk_vector.flatten(), r.flatten()) + message) % q
    
    return u, v

def kyber_decrypt(sk, ciphertext, q=3329):
    """Decrypt ciphertext"""
    u, v = ciphertext
    s = sk
    
    # Decrypt
    message = (v - np.dot(s.flatten(), u.flatten())) % q
    
    return message
Why It's Quantum-Resistant
No structure for Shor's algorithm: LWE doesn't involve factoring or discrete logs
Best known attack: BKZ lattice reduction (exponential time)
Quantum speedup: Minimal (Grover's algorithm only)
4. Hash-Based Signatures (SPHINCS+)
Concept
Uses only cryptographic hash functions (e.g., SHA-256)

Structure
text

One-Time Signatures (WOTS+)
    ↓
Few-Time Signatures (FORS)
    ↓
Hyper-Tree (SPHINCS+)
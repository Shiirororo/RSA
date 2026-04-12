# RSA Algorithm — Demo Project

## Table of Contents
- [Contributors](#contributors)
- [What is RSA?](#what-is-rsa)
- [How RSA Works](#how-rsa-works)
- [Project Structure](#project-structure)
- [Key Components](#key-components)
- [Usage](#usage)
---
## Contributors
- Pham Trieu Minh (20234026)
- Nguyen Trong Nhan (202414940)
- Tran Hoai Nam (20224412)
- Hoang Tuan Ngoc 
- Tran Phi Anh Nhat
- Do Hoai Nam 
---

## What is RSA?

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem widely used for secure data transmission. It relies on the mathematical difficulty of factoring the product of two large prime numbers.

RSA uses a **key pair**:
- **Public key** `(e, n)` — shared openly, used to encrypt.
- **Private key** `(d, n)` — kept secret, used to decrypt.

---

## How RSA Works

### 1. Key Generation

1. Choose two distinct large primes **p** and **q**.
2. Compute **n = p × q** (the modulus).
3. Compute **φ(n) = (p−1)(q−1)** (Euler's totient).
4. Choose **e** such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
5. Compute **d** as the modular inverse of e: `d ≡ e⁻¹ (mod φ(n))`.

> Public key: `(e, n)` | Private key: `(d, n)`

### 2. Encryption

Given plaintext integer **m** (where `m < n`):

```
c = m^e mod n
```

### 3. Decryption

Given ciphertext **c**:

```
m = c^d mod n
```

### 4. Mathematical Foundation

| Concept | Description |
|---|---|
| Modular Exponentiation | Fast computation of `base^exp mod n` using square-and-multiply |
| Extended Euclidean Algorithm | Finds `d` such that `e*d ≡ 1 (mod φ(n))` |
| Miller-Rabin Primality Test | Probabilistic test to verify large primes efficiently |

---

## Project Structure

```
ATTT/
├── main.py                  # Entry point
├── extendgcd.py             # Standalone extended GCD utility
│
├── RSA/
│   ├── __init__.py
│   └── rsa.py               # RSA class: key generation, encrypt, decrypt
│
├── Math/
│   ├── __init__.py
│   └── math.py              # Math utilities: gcd, extendedGCD, modExp, isPrime
│
├── tests/
│   ├── __init__.py
│   ├── test_rsa.py          # Unit tests for RSA
│   └── test_Math.py         # Unit tests for Math utilities
│
└── .github/
    └── workflows/
        └── test.yml         # CI pipeline (GitHub Actions)
```

---

## Key Components

### `Math/math.py` — `Math` class

| Method | Description |
|---|---|
| `gcd(a, b)` | Euclidean GCD |
| `extendedGCD(a, b)` | Extended Euclidean — returns `(gcd, x, y)` satisfying `ax + by = gcd` |
| `modExp(base, exp, mod)` | Fast modular exponentiation (square-and-multiply) |
| `isPrime(n, k=40)` | Miller-Rabin primality test, error probability ≤ `(1/4)^40` |

### `RSA/rsa.py` — `RSA` class

| Method | Description |
|---|---|
| `generate_keys()` | Generates `(e, n)` public key and `(d, n)` private key |
| `encrypt(message)` | Returns `m^e mod n` |
| `decrypt(ciphertext)` | Returns `c^d mod n` |

---

## Usage

```python
from RSA.rsa import RSA

rsa = RSA()

message = 42
ciphertext = rsa.encrypt(message)
plaintext  = rsa.decrypt(ciphertext)

print(f"Original : {message}")
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {plaintext}")
```

### Run tests

```bash
python -m pytest tests/
```

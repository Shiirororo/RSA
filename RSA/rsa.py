import random
from Math.math import Math


def generate_prime(start=100, end=300):
    while True:
        x = random.randint(start, end)
        if Math.isPrime(x):
            return x


def mod_inverse(a, m):
    g, x, _ = Math.extendedGCD(a, m)
    if g != 1:
        raise Exception("Không tồn tại nghịch đảo")
    return x % m


class RSA:
    def __init__(self):
        self.public_key, self.private_key = self.generate_keys()

    def generate_keys(self):
        # 1. sinh p, q
        p = generate_prime()
        q = generate_prime()
        while q == p:
            q = generate_prime()

        # 2. tính n, phi
        n = p * q
        phi = (p - 1) * (q - 1)

        # 3. chọn e
        e = 3
        while Math.gcd(e, phi) != 1:
            e += 2

        # 4. tính d
        d = mod_inverse(e, phi)

        return (e, n), (d, n)

    def encrypt(self, message):
        e, n = self.public_key
        return Math.modExp(message, e, n)

    def decrypt(self, ciphertext):
        d, n = self.private_key
        return Math.modExp(ciphertext, d, n)
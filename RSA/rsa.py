import secrets
from Math.math import Math




"""
Deprecated
"""

def generate_prime(num_bits=512):
    def generateRandom():
        # min_n_digit_number = 10**(num_digits - 1)
        # max_n_digit_number = 10**num_digits - 1
        while True:
            number = secrets.randbits(num_bits)
            number |= (1 << (num_bits - 1)) | 1
# - (1 << (num_bits - 1)): bit cao nhat (MSB) = 1 → dam bao co dung so num bit
# - | 1: bit thap nhat (LSB) = 1 → except 5
# - |= : con lai giu nguyen, OR lai de number la so le co bit dau la 1
            if number % 10 not in {1, 3, 7, 9}:     #Prime number la so le, khong co duoi 5
                continue
            return number
    count = 0
    while True:
        count += 1
        print(f"Iteration: {count}")
        number = generateRandom()
        if Math.millerRabin(number):
            return number

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
        print(f"Print number choose is: {p}, {q}")
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
    



# Sang nguyen to

# Select 
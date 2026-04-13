import secrets
from Math.math import Math




"""
Deprecated
"""

def generate_prime(num_bits=512):
    def generateRandom():
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
        manual = input("Ban co muon tu nhap p, q, e khong? (y/n): ").strip().lower() == 'y'

        if manual:
            while True:
                p = int(input("Nhap so nguyen to p: "))
                q = int(input("Nhap so nguyen to q: "))
                if not Math.millerRabin(p) or not Math.millerRabin(q):
                    print("p va q phai la so nguyen to. Thu lai.")
                elif p == q:
                    print("p va q phai khac nhau. Thu lai.")
                else:
                    break

            n = p * q
            phi = (p - 1) * (q - 1)

            while True:
                e = int(input(f"Nhap e (1 < e < {phi}, gcd(e, phi) = 1): "))
                if 1 < e < phi and Math.gcd(e, phi) == 1:
                    break
                print("Gia tri e khong hop le. Thu lai.")
        else:
            p = generate_prime()
            q = generate_prime()
            while q == p:
                q = generate_prime()
            print(f"Da sinh p = {p}, q = {q}")

            n = p * q
            phi = (p - 1) * (q - 1)
            while True:
                e = secrets.randbelow(phi)
                if Math.gcd(e, phi) == 1:
                    break

            while Math.gcd(e, phi) != 1:
                e += 2

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
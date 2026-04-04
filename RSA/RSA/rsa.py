import random

# Import các hàm toán học từ nhóm Bắt buộc

from Math.math import isPrime, gcd, extendedGCD, modExp

class RSA:
    def __init__(self, bit_length=1024):
        """
        Hàm khởi tạo: 
        """
        self.bit_length = bit_length
        self.public_key, self.private_key = self.generate_keys()

    def generate_keys(self):
        """
        Hàm nội bộ để tính toán p, q, n, e, d
        """
        # 1. Tìm p, q 
        # (Tạm gán bằng 0)
        p = 0 
        q = 0 
        
        # 2. Tính n và phi
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # 3. Tìm e(Tạm gán =3)
        e = 3 
        
        # 4. Tìm d
        d = extendedGCD(e, phi) 
        
        # Trả về 2 Tuple: Public Key (e, n) và Private Key (d, n)
        return (e, n), (d, n)

    def encrypt(self, message):
        """
        Hàm mã hóa: C = M^e mod n
        """
        # Lấy e và n từ public_key của chính đối tượng này
        e, n = self.public_key
        
        # Gọi hàm modExp 
        return modExp(message, e, n)

    def decrypt(self, ciphertext):
        """
        Hàm giải mã: M = C^d mod n
        """
        # Lấy d và n từ private_key của chính đối tượng này
        d, n = self.private_key
        
        # Gọi hàm modExp
        return modExp(ciphertext, d, n)
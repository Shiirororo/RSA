import secrets

class Math:
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    

    @staticmethod
    def extendedGCD(a, b):
        """
        Thuật toán Euclid mở rộng.
        Tìm Ước chung lớn nhất (GCD) của a và b, cùng với hai hệ số x, y 
        thỏa mãn phương trình Bézout: a*x + b*y = GCD(a, b).
        """
        # Khởi tạo các hệ số
        x0, x1, y0, y1 = 1, 0, 0, 1
        r0, r1 = a, b
        
        while r1 != 0:
            q = r0 // r1  # Thương số
            r0, r1 = r1, r0 % r1  # Cập nhật r0 và r1 mới (bước chia lấy dư)
            
            # Cập nhật các hệ số x và y
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
            
        # r0 lúc này chứa GCD, x0 và y0 là các hệ số Bézout
        return r0, x0, y0
    
    @staticmethod
    def modExp(base, exp, mod):
        """
        Hàm dùng chung cho cả mã hóa và giải mã RSA.
        
        Tham số:
        - base: Bản rõ (để mã hóa) hoặc Bản mã (để giải mã) dưới dạng số nguyên.
        - exp:  Khóa công khai (e) để mã hóa, hoặc khóa bí mật (d) để giải mã.
        - mod:    Module n (tích của 2 số nguyên tố p và q).
        
        Trả về:
        - Số nguyên là bản mã (nếu đang mã hóa) hoặc bản rõ (nếu đang giải mã).
        """
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp = exp //2
        return result



# Viec su dung isPrime cho cac so nho rat de. Tuy nhien de check cac so lon hon, ta su dung thuat toan Miller-Rabin
    @staticmethod
    def isPrime(n, k=40):       # Set k = 40. XS P(sai) <= (1/4)^k
        if n < 2:
            return False
        
        # các số nhỏ
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        if n in small_primes:
            return True
        if any(n % p == 0 for p in small_primes):
            return False

        # viết n-1 = d * 2^r
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1

        # test k lần (Miller-Rabin)
        for _ in range(k):
            # dùng secrets thay vì random
            a = secrets.randbelow(n - 3) + 2  # [2, n-2]

            x = pow(a, d, n)

            if x == 1 or x == n - 1:
                continue

            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False

        return True
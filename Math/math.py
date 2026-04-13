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


    #######DEPRECATED#######


    @staticmethod
    def isPrimeForSmallNumber(n):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


    @staticmethod
    def millerRabinIteration(n):
        a = secrets.randbelow(n-1)  # Dung secret thay cho random, chon a trong khoang [2, n-2]

        e = n - 1

        if Math.modExp(a, e, n) != 1: 
            return False
        prevIs1 = True
        while e%2 == 0:
            e //= 2
            x = Math.modExp(a, e, n)
            if prevIs1:
                if x == n-1: 
                    prevIs1 = False
                elif x!= 1: 
                    return False
        return True
    

    @staticmethod
    def millerRabin(n, k = 40):      # Set k = 40. XS P(sai) <= (1/4)^k
        for _ in range (k):
            if not Math.millerRabinIteration(n):
                return False
        return True

        #o(K LOG^3 R)

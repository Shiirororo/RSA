
#Merged, this file now unused

def extended_gcd(a, b):

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



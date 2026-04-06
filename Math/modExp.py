"""
    Hàm dùng chung cho cả mã hóa và giải mã RSA.
    
    Tham số:
    - base: Bản rõ (để mã hóa) hoặc Bản mã (để giải mã) dưới dạng số nguyên.
    - exp:  Khóa công khai (e) để mã hóa, hoặc khóa bí mật (d) để giải mã.
    - mod:    Module n (tích của 2 số nguyên tố p và q).
    
    Trả về:
    - Số nguyên là bản mã (nếu đang mã hóa) hoặc bản rõ (nếu đang giải mã).
    """
def modExp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp //2
    return result

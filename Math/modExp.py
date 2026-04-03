def modExp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp //2
    return result

print(modExp(2, 3, 5))
print(modExp(3, 4, 7))

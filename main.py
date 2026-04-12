from RSA.rsa import RSA

def main():
    print("RSA Encryption Demo")
    
    # 1. Tạo khóa RSA (tự động gen ra khóa public và khóa private)
    rsa = RSA()
    print(f"Public Key (e, n): {rsa.public_key}")
    print(f"Private Key (d, n): {rsa.private_key}")
    
    # 2. Thông điệp cần mã hóa
    message = 12345
    print(f"\nOriginal Message: {message}")
    
    # 3. Mã hóa thông điệp
    ciphertext = rsa.encrypt(message)
    print(f"Ciphertext: {ciphertext}")
    
    # 4. Giải mã thông điệp
    decrypted = rsa.decrypt(ciphertext)
    print(f"Decrypted Message: {decrypted}\n")
    
    # 5. Kiểm tra xem thông điệp có khớp với thông điệp ban đầu không
    if message == decrypted:
        print("Success! The decrypted message matches the original.")
    else:
        print("Error: The decrypted message does not match.")

if __name__ == "__main__":
    main()
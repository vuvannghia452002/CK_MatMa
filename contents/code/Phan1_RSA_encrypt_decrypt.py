def modinv(a, m):
    # Tìm số nghịch đảo d (nếu có) của a theo môđun m
    # https://vi.wikipedia.org/wiki/Gi%E1%BA%A3i_thu%E1%BA%ADt_Euclid_m%E1%BB%9F_r%E1%BB%99ng
    y0, y1, original_m = 0, 1, m  
    
    while a > 0:
        r = m % a
        if r == 0:
            break
        q = m // a
        y = y0 - y1 * q
        y0, y1 = y1, y
        m, a = a, r
    
    if a > 1:
        return "A không khả nghịch theo môđun m"
    else:
        return y1 % original_m  

def rsa_encrypt(M, e, n):
    return pow(M, e, n)

def rsa_decrypt(C, d, n):
    return pow(C, d, n)

p=int(input(f"Nhập giá trị p: "))
q=int(input(f"Nhập giá trị q: "))

n = p * q
phi_n = (p - 1) * (q - 1)  
print(f"n = {n}, phi_n = {phi_n}")

print(f"Chọn e sao cho gcd(e, phi_n) = 1")
e=int(input(f"Nhập giá trị e: "))

print(f"Tìm d sao cho d * e ≡ 1 (mod phi_n)")
d = modinv(e, phi_n)   
print(f"d = {d}")

print(f"Khóa công khai (n, e) = ({n}, {e})")
print(f"Khóa bí mật (n, d) = ({n}, {d})")

m=int(input(f"Nhập giá trị bản rõ m: "))
c = rsa_encrypt(m, e, n)
print(f"Mã hóa: m = {m} -> c = {c}")
decrypted_M = rsa_decrypt(c, d, n)
print(f"Giải mã: c = {c} -> m = {decrypted_M}")

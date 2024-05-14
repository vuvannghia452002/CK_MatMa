def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def rsa_encrypt(M, e, n):
    return pow(M, e, n)

def rsa_decrypt(C, d, n):
    return pow(C, d, n)

# Thông số RSA
p = 11
q = 3
n = p * q  # n = 33
phi_n = (p - 1) * (q - 1)  # phi_n = 20

e = 3  # chọn e sao cho gcd(e, phi_n) = 1

# Tìm d sao cho d * e ≡ 1 (mod phi_n)
d = modinv(e, phi_n)  # d = 7

# Khóa công khai (n, e) và khóa bí mật (n, d)
public_key = (n, e)
private_key = (n, d)

# Bản rõ
M = 15

# Mã hóa
C = rsa_encrypt(M, e, n)
print(f"Mã hóa: M = {M} -> C = {C}")

# Giải mã
decrypted_M = rsa_decrypt(C, d, n)
print(f"Giải mã: C = {C} -> M = {decrypted_M}")

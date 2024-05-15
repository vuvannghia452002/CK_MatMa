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

p=int(input(f"Nhập giá trị p: "))
q=int(input(f"Nhập giá trị q: "))

n = p * q
phi_n = (p - 1) * (q - 1)  
print(f"🚀 n = {n}, phi_n = {phi_n}")

print(f"🚀 Chọn e sao cho gcd(e, phi_n) = 1")
e=int(input(f"Nhập giá trị e: "))

print(f"🚀 Tìm d sao cho d * e ≡ 1 (mod phi_n)")
d = modinv(e, phi_n)   

print(f"🚀 Khóa công khai (n, e) = ({n}, {e})")
print(f"🚀 Khóa công khai (n, d) = ({n}, {d})")

m=int(input(f"Nhập giá trị bản rõ m: "))

c = rsa_encrypt(m, e, n)

print(f"Mã hóa: m = {m} -> c = {c}")

decrypted_M = rsa_decrypt(c, d, n)
print(f"Giải mã: c = {c} -> m = {decrypted_M}")

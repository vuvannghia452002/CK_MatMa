import math
import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def get_prime(size):
    while True:
        n = random.randint(size, 2*size)
        if is_prime(n):
            return n


def phi(a, b):
    return a*b//math.gcd(a, b)


def get_e(phi_n):
    for i in range(2, phi_n):
        if math.gcd(i, phi_n) == 1:
            return i
    return 0


def get_d(e, phi_n):
    for i in range(1, phi_n):
        if (e*i) % phi_n == 1:
            return i
    return 0


# if __name__ == '__main__':
size = 300

p = get_prime(size)
q = get_prime(size)
print(f"p = {p}, q = {q}")


n = p * q
print(f"n = {n}")


phi_n = phi(p-1, q-1)
print(f"phi_n = {phi_n}")


e = get_e(phi_n)
print(f"e = {e}")


d = get_d(e, phi_n)
print(f"d = {d}")



print(f"Public key (e,n) = ",e,n)

print(f"Private key (d,n) = ",d,n)



m=117
c=m**e % n

print(f"m = {m}, c = {c}")

m=c**d % n

print(f"m = {m}, c = {c}")
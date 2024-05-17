from math import sqrt
import random


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def getPrime(size):
    while True:
        n = random.randint(size, 2*size)
        if isPrime(n):
            return n

# if __name__ == '__main__':

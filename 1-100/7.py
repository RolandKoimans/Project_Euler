import math

def FindPrime(num):
    count = 0
    i = 1
    while count <= num:
        if IsPrime(i):
            count += 1
        i += 1
    return i-1 

def IsPrime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(FindPrime(10001))
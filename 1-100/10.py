import math

def PrimeSummation(rangeVal):
    summation = 0
    for i in range(2,rangeVal):
        if IsPrime(i):
            summation += i
    
    return summation

def IsPrime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(PrimeSummation(2000000))
import math
# Prime factorization algorithm from geeksbygeeks
def LargestFactor(num):
    factors = []
    
    while num % 2 == 0:
        num = num / 2
        factors.append(2)
    
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            factors.append(i)
            num = num / i

    if num > 2:
        factors.append(num)

    factors.sort(reverse=True)
    return factors[0]    

if __name__ == '__main__':
    print(LargestFactor(600851475143))

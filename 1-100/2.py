def EvenFib(maxVal):
    sum = 0
    prev1 = 1
    prev2 = 0
    cur = 0
    while cur < maxVal:
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
        if cur % 2 == 0:
            sum+= cur 
    return sum

if __name__ == '__main__':
    print(EvenFib(4000000)) 
def SmallestMultiple():
    cur = 20
    while True:
        evenDiv = True
        for i in reversed(range(1,21)):
            if cur % i != 0:
                evenDiv = False
            if not evenDiv:
                break
        if evenDiv:
            return cur
        # Target must be a multiplication of 20
        cur += 20
    return -1

if __name__ == '__main__':
    print(SmallestMultiple())
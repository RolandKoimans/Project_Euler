def PythTriplet():
    for c in range(2,1000):
        for b in range(1,c):
            for a in range(1,b):
                if (a**2 + b**2 == c**2) and (a + b + c == 1000):
                    return a*b*c
    return -1

if __name__ == '__main__':
    print(PythTriplet())
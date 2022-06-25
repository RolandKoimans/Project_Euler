import math

def SumSquare(num):
    sumOfSquares = 0
    for i in range(1,num+1):
        sumOfSquares += i ** 2

    squareOfSum = 0
    for i in range(1,num+1):
        squareOfSum += i
    squareOfSum = squareOfSum ** 2


    return squareOfSum - sumOfSquares

if __name__ == '__main__':
    print(SumSquare(100))


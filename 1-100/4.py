import math

# Determines the largest palindrome by iterating all product values
def LargestPal(digits):
    maxVal = 0
    for i in range(int(math.pow(10,digits))):
        for j in range(int(math.pow(10,digits))):
            if(IsPal(i*j)):
                maxVal = max(maxVal, i * j)
    return maxVal

# Checks if a number is a palindrome
def IsPal(num):
    numList = Split(str(num))

    # Lenght of the to be searched element is half on both sides, rounded down because if odd, the middle element doesn't matter
    length = int(len(numList) / 2)

    if length == 0:
        return True

    for i in range(length):
        if(numList[i] != numList[-(i+1)]):
            return False
    
    return True

# Split a number into a list of digits using list comprehension
def Split(number):
    return [num for num in number]

if __name__ == '__main__':
    print(LargestPal(3))

from ast import AsyncFunctionDef

def MultiplesSum(num):
    result = 0
    for cur in range(num):
        if (cur % 3 == 0) or (cur % 5 == 0):
            result+= cur 
    return result

if __name__ == '__main__':    
    print(MultiplesSum(1000))

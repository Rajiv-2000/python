def sumOfNumbersRecursive(N):
    """Add all the integers from 1 to given number N recursively"""
    if N == 0:
        return 0
    else:
        result = N + sumOfNumbersRecursive(N - 1)
        return result
    
N = int(input("Enter a number: "))
print(sumOfNumbersRecursive(N))

#learn fucntion and DataTypes

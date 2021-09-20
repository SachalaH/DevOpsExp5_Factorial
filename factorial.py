# Python 3 program to find
# factorial of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact


# Driver Code
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    print("Factorial of", num, "is", factorial(num))

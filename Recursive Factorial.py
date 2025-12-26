def is_factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*is_factorial(n-1)
result = is_factorial(5)
print(result)

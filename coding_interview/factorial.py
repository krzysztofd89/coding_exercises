def factorial_recursive(n):
    if n in (0, 1):
        return 1
    else:
        return n*factorial_recursive(n-1)


def factorial_iterative(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial


print(factorial_recursive(6))
print(factorial_iterative(6))

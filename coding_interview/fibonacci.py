def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    if n < 2:
        return n
    else:
        fib_1, fib_2 = 0, 1
        for j in range(2, n+1):
            fib_1, fib_2 = fib_2, fib_1+fib_2
        return fib_2


for i in range(10):
    print(f'fibonacci - {i}')
    print(fibonacci_recursive(i))
    print(fibonacci_iterative(i))

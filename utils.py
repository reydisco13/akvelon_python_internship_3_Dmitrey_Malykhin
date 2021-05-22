def fibonacci(n):
    if n in [1,2]:
        return 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
    return res

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        return res

resultado = fibonacci(7)

print(resultado)
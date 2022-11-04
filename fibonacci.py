def fib(n):
    # Catch negative numbers
    if n <= 0:
        raise ValueError("Non positive numbers are not allowed")

    # Catch non-integers
    if not isinstance(n, int):
        raise TypeError("Only integers are allowed")
    
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
        
    return a
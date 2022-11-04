def fizzbuzz(n):
    # Catch negative numbers
    if n < 0:
        raise ValueError("Negative numbers are not allowed")

    # Catch non-integers
    if not isinstance(n, int):
        raise TypeError("Only integers are allowed")
        
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
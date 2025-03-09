# Check Even or Odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# Swap Two Numbers
def swap_numbers(a, b):
    return b, a

# Nth Term of AP
def nth_term_ap(a, d, n):
    return a + (n - 1) * d

# Reverse Digits of an Integer
def reverse_integer(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

# Primality Test
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check Triangle Validity
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Prime Factors of an Integer
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# Example usage
print(check_even_odd(10))  # Even
print(swap_numbers(3, 5))  # (5, 3)
print(nth_term_ap(2, 3, 5))  # 14
print(reverse_integer(1234))  # 4321
print(is_prime(17))  # True
print(is_valid_triangle(3, 4, 5))  # True
print(factorial(5))  # 120
print(prime_factors(56))  # [2, 2, 2, 7]


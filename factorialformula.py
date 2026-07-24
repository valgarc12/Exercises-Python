"""
Given a number n, write a formula that returns n!."""

def factorial(n):
    result = 1
    if n == 0:
        return 1
    while n > 0:
        result *= n
        n = n - 1
    return result    
        
print(factorial(5))
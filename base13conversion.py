"""
Instructions:
Given an integer num, return its string representation in base 13.

In case you don't use base 13 that much (who does, right?), here's a quick rundown: just like base 10 uses digits from 0 to 9. But also for 10, 11 and 12, we use the letters A, B, and C.

For example:

9 in base 13 is still "9"
10 in base 13 is "A"
11 in base 13 is "B"
12 in base 13 is "C"
13 in base 13 is "10"
14 in base 13 is "11"
49 in base 13 is "3A" (since 49 = 3 * 13 + 10, and 10 is represented as "A")
"""

def conversion13(num):
    base13 = "0123456789ABC"
    result = ""

    abs_num = abs(num)
    while abs_num > 0:
        module = abs_num % 13
        result += base13[module]
        abs_num = abs_num // 13
        
    if num > 0:
        result = result[::-1]
    elif num == 0:
        return "0"
    else:
        result = "-" + result[::-1]        
    return result

numero = int(input('Cuál número quieres convertir: '))

print(conversion13(numero))
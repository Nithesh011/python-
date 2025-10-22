def is_armstrong(n: int):
    if n < 0:
        return f"Please enter a positive integer"
    
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == n:
        return f"True: {n} is an Armstrong number"
    else:
        return f"False: {n} is not an Armstrong number"

n = 153
print(is_armstrong(n))

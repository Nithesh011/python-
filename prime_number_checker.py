def find_prime(n:int):
    if n <= 1:
        return f"Please enter the natural number to check prime"
    i=2
    while i*i <= n:
        if n % i == 0:
            return f"False :The given number {n} is not a prime number"
        i += 1
    return f"True:The given number {n} is a prime number"
n=5
print(find_prime(n))

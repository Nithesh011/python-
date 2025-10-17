def fact(n:int):
    if n<=0:
        return f"Please enter number above zero for check the factorial"
    result=1
    for i in range(1,n+1):
        result*=i
    return f"The factorial of {n} is {result}"
        
n=3
print(fact(n))

def palindrome(n):
    n=n.replace(" ","")
    c=""
    j=1
    for i in range(len(n)):
        c+=(n[len(n)-j])
        j+=1
    if n.lower()==c.lower():
        return f"The given string is Palindrome:{n}"
    else:
        return f"Sorry the given string is not a Palindrome:{n}"
r='race car'
print(palindrome(r))

# Find the lexicographically largest substring in a given string
s = "welcome"
c = s[0]
for i in range(len(s)):
    for j in range(i, len(s)):
        r = s[i:j+1]
        if r > c:
            c = r
print(c)

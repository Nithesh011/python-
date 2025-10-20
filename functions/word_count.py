def word_count(str1):
    s = str1.split()
    j = {}
    for i in s:
        if i in j:
            j[i] += 1
        else:
            j[i] = 1
    print(j)
    for i, r in j.items():
        print(i, r)
    y = next(iter(j))
    print(y)


# Example usage
str1 = "aaa bbb ccc aaa ddd ccc aaa"
word_count(str1)

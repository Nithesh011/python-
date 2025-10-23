def word_count(str1):
    s = str1.split()
    j = {}
    for i in s:
        if i in j:
            j[i] += 1
        else:
            j[i] = 1
    return j


str1 = "aaa bbb ccc aaa ddd ccc aaa"
counts = word_count(str1)
print(counts)

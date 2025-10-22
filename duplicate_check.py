nums = [1, 2, 3, 1]
s = set()  # to keep track of numbers we have seen

for i in nums:
    if i in s:
        print(True)  # duplicate found
        break
    s.add(i)  # add number to set

else:
    print(False)  # no duplicates found

def removeduplicates(nums:list):
    c=[]
    for i in nums:
        if i not in c:
            c.append(i)
    return c

nums = [3, 5, 2, 3, 8, 2, 9]
print(removeduplicates(nums))
        
        

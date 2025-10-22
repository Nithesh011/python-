def findpair(n:list ,target:int):
    r=[]
    for i in range(len(n)):
        for j in range(i,len(n)):
            if n[i]+n[j]==target and n[i]!=n[j]:
                r.append((n[i],n[j]))
    return r
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10
print(findpair(nums,target))

def twosum(n,target):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if target==n[i]+n[j]:
                return ([i,j])
                break
target=4
n=[1,2,3,5,6,8]
print(twosum(n,target))
--------------------------------------------------------------------OR-----------------------------------------------------------------------------------------------------------------------------

def twosum(num,target):
    dict={}
    for i,j in enumerate(num):
        answer=target-j
        if answer in dict:
            return f"Answer is {[dict[answer],i]}"
        else:
            dict[j]=i
number=[3,2,5,6,7]
target=10
print(twosum(number,target))

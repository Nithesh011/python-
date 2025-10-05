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

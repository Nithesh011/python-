def largestsecondnumber(n:list):
    second_max=max_num=float('-inf')
    for i in n:
        if i>max_num:
            second_max=max_num
            max_num=i
        elif i>second_max and i!=max_num:
            second_max=i
    return f"The second largest number in the list is {second_max}"
nums = [10, 5, 2, 1]
print(largestsecondnumber(nums))

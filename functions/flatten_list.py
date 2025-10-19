def nested_list(n:list):
    flat=[]
    for i in n:
        if isinstance(i,list):
            flat.extend(nested_list(i))
        else:
            flat.append(i)
    return flat
            

input = [1, [2, [3, 4], 5], 6]
print(nested_list(input))

temps = [30, 32, 31, 29, 35, 36]
a = []

for i in range(2, len(temps)): 
    r = round(sum(temps[i-2:i+1]) / 3, 2)
    a.append(r)

print(a)

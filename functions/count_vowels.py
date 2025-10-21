def count_vowels(n):
    if not isinstance(n, str):
        return "Please enter a string. Thank you."

    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = {}
    
    for i in n.lower():
        if i in vowels:
            counts[i] = counts.get(i, 0) + 1
    
    total = sum(counts.values())
    return f"Total vowels: {total}\nBreakdown: {counts}"

print(count_vowels("Hello World"))

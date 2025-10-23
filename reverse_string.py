def reverse_string(s: str) -> str:
    r = ""
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return f"The Given String is: {s}\nThe string has been reversed: {r}"

Input = "hello"
print(reverse_string(Input))

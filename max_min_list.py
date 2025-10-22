# File: max_min_list.py
# Description: Find the maximum and minimum elements in a list without using built-in max() or min().

def maxmin(nums: list):
    # Initialize min and max with the first element
    min_num = nums[0]
    max_num = nums[0]

    # Traverse the list to find min and max
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    # Return formatted string
    return f"Minimum: {min_num}\nMaximum: {max_num}"

# Example usage
n = [2, 4, 6, 9, 8, 5, 1]
print(maxmin(n))

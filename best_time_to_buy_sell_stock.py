# Problem: Best Time to Buy and Sell Stock
# Author: Nithesh Kumar S
# Date: 2025-10-06
# Description: Find the maximum profit from stock prices where you must buy before selling.

c = [1, 2, 3, 4, 5]
max_profit = 0

for i in range(len(c)):
    for j in range(i + 1, len(c)):
        profit = c[j] - c[i]
        if profit > max_profit:
            max_profit = profit

print("Maximum Profit:", max_profit)

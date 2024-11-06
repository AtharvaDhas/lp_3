class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(w, arr):
    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    finalValue = 0.0
    for item in arr:
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w/item.weight)
            break
    return finalValue

if __name__ == "__main__":
    n = int(input("Enter number of items-\n"))
    arr = []
    for i in range(n):
        profit = int(input("Enter profit of item " + str(i + 1) + "-\n"))
        weight = int(input("Enter weight of item " + str(i + 1) + "-\n"))
        arr.append(Item(profit, weight))
    w = int(input("Enter capacity of knapsack-\n"))
    print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))

































#     Concept of Fractional Knapsack
# The fractional knapsack problem is a variation of the classical knapsack problem. The goal is to maximize the total value of items packed in a knapsack with a weight limit. The difference here is that you can take fractions of items, rather than being limited to taking whole items or none at all.

# In simpler terms, if you have a knapsack that can carry a certain weight, you want to fill it with the most valuable items, or parts of items, without exceeding its weight limit. The idea is to take as much of an item as you can, based on how valuable it is per unit of weight.

# Explanation of the Code (Step-by-Step)
# Defining the Item Class:

# python
# Copy code
# class Item:
#     def __init__(self, profit, weight):
#         self.profit = profit
#         self.weight = weight
# This class is used to create an "item" that has two properties:
# profit: the value (or profit) you get from the item.
# weight: how much the item weighs.
# For example, an item might have a profit of 60 and weigh 10 units.
# fractionalKnapsack function:

# python
# Copy code
# def fractionalKnapsack(w, arr):
#     arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
#     finalValue = 0.0
#     for item in arr:
#         if w >= item.weight:
#             finalValue += item.profit
#             w -= item.weight
#         else:
#             finalValue += item.profit * (w/item.weight)
#             break
#     return finalValue
# Input: w is the maximum capacity (weight) of the knapsack, and arr is a list of Item objects (each having profit and weight).
# Sorting the Items:
# The items are sorted based on the profit-to-weight ratio. This ratio represents how much profit you get for each unit of weight. Higher ratios are better, so the items with the best ratio come first.
# For example, if one item has a profit of 60 and weighs 10, its ratio is 60/10 = 6. Another item might have a ratio of 5.
# Filling the Knapsack:
# It goes through the sorted items one by one. If the item’s weight is less than or equal to the remaining capacity (w) of the knapsack, it takes the full item, adding its full profit to the total.
# If the item doesn’t fully fit, it takes as much of the item as possible (a fraction of it) and adds the corresponding fraction of the profit.
# It stops when the knapsack is full (i.e., no more capacity).
# Return: The function returns the maximum profit that can be achieved.
# Example: Let's say you have:

# Items with profits and weights:
# Item 1: profit = 60, weight = 10 (ratio = 6)
# Item 2: profit = 100, weight = 20 (ratio = 5)
# Item 3: profit = 120, weight = 30 (ratio = 4)
# Knapsack capacity: 50 units.
# Steps:

# Sort the items based on the profit/weight ratio: Item 1 (6), Item 2 (5), Item 3 (4).
# Add the full Item 1 (weight 10, profit 60) → Remaining capacity = 50 - 10 = 40.
# Add the full Item 2 (weight 20, profit 100) → Remaining capacity = 40 - 20 = 20.
# Add a fraction of Item 3. You can only take 20 units (since that's all that's left in the knapsack), which is 2/3 of the full item. The profit from this fraction would be 
# 120
# ×
# (
# 20
# /
# 30
# )
# =
# 80
# 120×(20/30)=80.
# The total profit = 60 + 100 + 80 = 240.
# Main Block:

# python
# Copy code
# if __name__ == "__main__":
#     n = int(input("Enter number of items-\n"))
#     arr = []
#     for i in range(n):
#         profit = int(input("Enter profit of item " + str(i + 1) + "-\n"))
#         weight = int(input("Enter weight of item " + str(i + 1) + "-\n"))
#         arr.append(Item(profit, weight))
#     w = int(input("Enter capacity of knapsack-\n"))
#     print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))
# This part is responsible for interacting with the user. It asks the user for:
# The number of items.
# The profit and weight of each item.
# The knapsack’s capacity.
# After gathering the input, it calls the fractionalKnapsack function and prints out the maximum value that can be placed in the knapsack.
# Summary:
# The goal of this program is to help you fill a knapsack with items (or fractions of them) in a way that maximizes the total value. The key concept is the profit-to-weight ratio—items that give you more value for their weight are prioritized.

# This solution uses the greedy approach, where decisions are made to maximize the immediate benefit at each step (i.e., taking the item with the highest ratio first).
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

values = [60, 100, 120]  
weights = [10, 20, 30]   
capacity = 50            

max_value = knapsack(values, weights, capacity)
print(f'Maximum value in the knapsack: {max_value}')








































# Problem Concept:
# The 0/1 Knapsack Problem is a well-known optimization problem. You have a set of items, each with a certain value and weight. Your goal is to maximize the total value of the items you pick, without exceeding a given weight capacity for the knapsack (a bag that can carry items).

# In simple terms:

# You want to pack the knapsack with items such that the total value is as high as possible.
# The total weight of the items you select should not exceed the knapsack's capacity.
# Code Walkthrough:
# 1. Function Definition:
# python
# Copy code
# def knapsack(values, weights, capacity):
# This function takes three parameters:
# values: A list of the values of the items.
# weights: A list of the weights of the items.
# capacity: The maximum weight the knapsack can carry.
# 2. Creating the DP Table:
# python
# Copy code
# dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
# We create a 2D array dp (dynamic programming table) of size (n+1) x (capacity+1) where:
# n is the number of items (length of the values or weights list).
# capacity is the maximum weight that can be carried by the knapsack.
# The idea of this table is to store the maximum value that can be obtained for each subset of items and knapsack capacities.
# 3. Filling the DP Table:
# python
# Copy code
# for i in range(1, n + 1):
#     for w in range(1, capacity + 1):
# We loop through all the items (i from 1 to n) and all possible knapsack capacities (w from 1 to capacity).
# 4. Decision: Include or Exclude the Item:
# python
# Copy code
# if weights[i - 1] <= w:
#     dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
# else:
#     dp[i][w] = dp[i - 1][w]
# For each item, we check if the item's weight (weights[i-1]) is less than or equal to the current knapsack capacity w.
# If the item can fit in the knapsack, we consider two options:
# Don't take the item: The maximum value is the same as the previous item (dp[i-1][w]).
# Take the item: Add the item's value to the best possible value for the remaining capacity (dp[i-1][w - weights[i-1]] + values[i-1]).
# We pick the best of these two options using the max() function.
# If the item can't fit, we simply keep the previous value (dp[i-1][w]), meaning we exclude the item.
# 5. Return the Final Result:
# python
# Copy code
# return dp[n][capacity]
# The final answer (the maximum value the knapsack can carry with the given capacity) is stored at dp[n][capacity] — i.e., the maximum value obtainable using all items and the full capacity of the knapsack.
# Example Walkthrough:
# For the following example:

# python
# Copy code
# values = [60, 100, 120]  
# weights = [10, 20, 30]   
# capacity = 50
# Item Details:

# Item 1: Value = 60, Weight = 10
# Item 2: Value = 100, Weight = 20
# Item 3: Value = 120, Weight = 30
# Knapsack Capacity = 50

# Now, we try to maximize the value by deciding which items to include or exclude at each step. The dynamic programming table is filled with the best value for every combination of items and capacities.

# At the end, the value dp[3][50] holds the maximum value for all 3 items and a knapsack capacity of 50.
# In this case, the optimal items to pick would be Item 2 (Value = 100, Weight = 20) and Item 3 (Value = 120, Weight = 30), giving a total value of 220.
# Why Dynamic Programming?
# Dynamic programming (DP) is used here because it breaks the problem into smaller subproblems and stores the results of those subproblems to avoid redundant calculations. Without DP, we'd have to re-calculate the same subproblem multiple times, which would be inefficient.

# This approach is much faster than brute-force (which would check all possible combinations of items).

# Summary:
# The Knapsack problem is about finding the best combination of items (based on their weight and value) that fit within a specific weight limit.
# The code uses dynamic programming to efficiently solve the problem by breaking it down into smaller subproblems, storing their solutions, and reusing them to build up the final answer.
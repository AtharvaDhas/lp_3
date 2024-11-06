def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
n = 10
recursive_results = [fibo(i) for i in range(n)]
iterative_results = [iterative(i) for i in range(n)]
print(iterative_results)
print(recursive_results)
























# # This code is designed to calculate Fibonacci numbers using two different methods: recursion and iteration. Let's break it down in a simple, human way:

# What are Fibonacci numbers?
# Fibonacci numbers form a sequence where each number is the sum of the two preceding ones. The sequence starts with 0 and 1, and it continues like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Mathematically, the rule to generate the Fibonacci sequence can be expressed as:

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1
# Code Overview
# 1. Recursive Function: fibo(n)
# Recursion means a function calls itself to solve smaller parts of the problem. Here's how this works:

# Base Case: If n is 0 or 1, it simply returns n. This stops the recursion from going further.
# Recursive Case: If n is greater than 1, it calls itself twice: once with n-1 and once with n-2, adding the results of these two calls together.
# How does it work?
# For example, to calculate fibo(4):

# The function will call fibo(3) and fibo(2)
# To calculate fibo(3), it calls fibo(2) and fibo(1)
# This continues until it reaches the base cases (fibo(1) and fibo(0)), which return 1 and 0 respectively.
# 2. Iterative Function: iterative(n)
# Iteration means using a loop to calculate the result step-by-step without calling the function again.

# Base Case: If n is 0 or 1, it returns n directly (same as the recursive method).
# Loop: If n is greater than 1, it uses a loop to calculate the Fibonacci number. It starts with the first two numbers (0 and 1), then repeatedly adds them to generate the next number in the sequence.
# How does it work?
# To calculate iterative(4):

# Start with a = 0 and b = 1 (the first two Fibonacci numbers).
# In each loop iteration, you update a and b:
# In the first iteration, a becomes 1, and b becomes 1.
# In the second iteration, a becomes 1, and b becomes 2.
# In the third iteration, a becomes 2, and b becomes 3.
# At the end of the loop, b holds the value of the 4th Fibonacci number (3).
# Key Concept: Recursion vs. Iteration
# Recursion: The function calls itself repeatedly, which can lead to repeated calculations (like recalculating fibo(2) several times). This makes the recursive method less efficient for larger inputs because it takes a long time and uses more memory.
# Iteration: The loop-based method is more efficient since it calculates each Fibonacci number only once, updating variables along the way. This makes it much faster and better suited for large inputs.
# In summary:

# The recursive method is simple but can be slow for large numbers due to repeated calculations.
# # The iterative method is more efficient because it avoids those repeated calculations by using a loop to directly calculate each Fibonacci number.
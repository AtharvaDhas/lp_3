import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def printNodes(node, val=""):
    newval = val + node.huff
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    else:
        print(f"{node.symbol} -> {newval}")

chars = ["a", "b", "c", "d", "e", "f"]
freqs = [5, 9, 12, 13, 16, 45]
nodes = []

for i in range(len(chars)):
    heapq.heappush(nodes, node(freqs[i], chars[i]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = "0"
    right.huff = "1"
    newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newnode)

printNodes(nodes[0])























# Concept of Huffman Coding:
# Imagine you want to send a message using as little data as possible, but without losing any information. Huffman coding helps with that. The idea is to give shorter codes to more frequent symbols (like letters in a text) and longer codes to less frequent symbols. This way, the most common symbols take up less space, and you end up with an efficient way to compress data.

# Huffman coding works by creating a tree (called a Huffman tree), where:

# Each leaf node represents a symbol (like a letter).
# The path from the root to a leaf gives the binary code for that symbol.
# More frequent symbols have shorter paths (codes) in the tree.
# What’s happening in the code:
# 1. Building a Tree Using Frequencies
# Imagine you have some letters with different frequencies:

# Letters that appear more often should get shorter codes.
# Letters that appear less often will get longer codes.
# So we build a tree in a way that the letters with lower frequencies are combined first, and the tree grows based on the frequency of each letter.

# 2. The node Class
# This is like a blueprint for the tree nodes. Each node stores:
# freq (frequency) — how often this letter (or group of letters) appears.
# symbol — the letter(s) it represents.
# left and right — pointers to its child nodes (since it’s a tree).
# huff — this stores whether the node's path in the tree is a "0" (left) or "1" (right).
# 3. Creating the Heap (Priority Queue)
# A heap is a kind of list where the smallest (or highest priority) item is always at the top.

# We take all the letters and their frequencies, make node objects out of them, and push them into this heap.
# The heap always ensures that the node with the smallest frequency stays on top, so we can combine them easily later.
# 4. Building the Huffman Tree
# Now we start building the tree. Here’s how it works:

# We take the two nodes with the smallest frequencies from the heap.
# We combine them to make a new node, whose frequency is the sum of the two smaller ones.
# We give the left child a huff = "0" and the right child a huff = "1". This builds the binary encoding bit by bit.
# Repeat this process until there’s just one node left in the heap—this is your complete Huffman tree.

# 5. Printing the Codes
# Once the tree is built, we traverse it from top to bottom. Every time we go left, we add a "0" to the code, and every time we go right, we add a "1". When we reach a leaf node (a letter), we print out the code we’ve built for that letter.

# Example in a Real-Life Scenario:
# Let’s say you have the following letters and frequencies:

# a (5 times)
# b (9 times)
# c (12 times)
# d (13 times)
# e (16 times)
# f (45 times)
# The more frequent the letter (like f), the shorter its code. This code allows us to compress a text that uses these letters without losing any data.

# Human Analogy:
# Imagine you’re packing for a trip. You pack the things you use the most in smaller, easy-to-access places (like your phone or wallet). Things you don’t need as often go into bigger, harder-to-reach places (like a suitcase). Huffman coding is similar. The things (letters) you use the most get the smallest "pockets" (short codes). Things you use less often (less frequent letters) get bigger "pockets" (longer codes).

# How Huffman Coding Helps:
# It compresses data by using fewer bits for common symbols.
# It’s widely used in file compression algorithms like ZIP files or in image formats like JPEG, where reducing the size of data is important.
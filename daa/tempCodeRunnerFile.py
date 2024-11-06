

#         The Problem:
# The N-Queens problem asks you to place n queens on an n x n chessboard such that:

# No two queens share the same row.
# No two queens share the same column.
# No two queens are on the same diagonal.
# For example, on an 8x8 chessboard, you need to place 8 queens so that none of them can attack each other.

# Concept of the Solution (Backtracking):
# The code uses a technique called backtracking, which is like trying one option, and if it leads to a dead end (no more valid moves), it goes back (backtracks) and tries another option. In this case, it’s trying to place queens on the board in a way that satisfies the problem’s conditions.

# Think of backtracking as a trial-and-error process where the program places queens one-by-one in each row, and if it finds a conflict (i.e., two queens threatening each other), it removes the queen and tries a different column.

# How the Code Works:
# Initial Setup:

# You start with an empty chessboard (represented by a 2D array board), where each cell can either have a queen ("Q") or be empty (".").
# You also use three sets to track which columns and diagonals are already occupied by a queen:
# col: Keeps track of columns where queens are placed.
# posDiag: Tracks diagonals that go from the top-left to the bottom-right.
# negDiag: Tracks diagonals that go from the top-right to the bottom-left.
# Placing the First Queen:

# Before starting the recursive search, the first queen is placed at a specific column (first_queen_col) on the first row (r = 0).
# The program adds the column and the diagonals of the first queen to the respective sets (col, posDiag, negDiag) to mark them as occupied.
# Backtracking Function (backtrack):

# The function backtrack(r) is responsible for placing queens row by row, starting from the second row (r = 1).
# For each row r, it tries placing a queen in each column (c).
# It checks if placing a queen at (r, c) would cause a conflict with another queen. This is done by:
# Checking if c is already occupied (using col).
# Checking if the diagonals are already occupied (using posDiag and negDiag).
# If no conflict, it places a queen at position (r, c) and marks the column and diagonals as occupied.
# It then moves on to the next row (r + 1) and continues trying to place queens.
# If it reaches the end (r == n), it means all queens have been placed successfully, and the board configuration is saved as a valid solution.
# If a conflict is detected at any point, it removes the queen and tries the next column (backtracking).
# Backtracking (Undoing Choices):

# If placing a queen leads to a dead end (i.e., no valid columns to place a queen in the next row), it removes the queen from the current row and unmarks the occupied columns and diagonals.
# It then tries the next column in the current row, continuing the search for a valid solution.
# Output:

# Once all solutions are found, the function returns the list of valid chessboard configurations.
# The main program then prints the first valid solution in a readable format, showing where the queens are placed.
# The Key Idea of Backtracking:
# The main concept behind backtracking is trial and error. You try a possible solution, and if it doesn’t work, you “backtrack” and try a different path. In this case:
# Try placing a queen in each row, and if a valid position is found, move to the next row.
# If you find a conflict, undo the current placement and try a different position in the same row.
# This process continues until you either find a solution or exhaust all options.
# Simplified Example:
# Let's take a 4x4 board and walk through it:

# Place the first queen on row 0, column 1.
# In the second row, check each column. Place a queen in a column that doesn’t conflict with the first queen.
# Continue to place queens row by row.
# If you can’t place a queen without a conflict, backtrack and move the queen to a different column.
# When all queens are placed, save the configuration as a valid solution.
# Visualizing Backtracking:
# Imagine the backtracking process as trying to fill a series of boxes (rows) one by one.
# If a box is filled in a way that no longer works (because of conflicts), you go back to the previous box, change the choice, and continue.
# Why Backtracking Works Here:
# The N-Queens problem has a lot of potential configurations, but many of them are invalid (queens attacking each other).
# Backtracking helps to efficiently explore the possible configurations, discarding invalid paths early (by removing queens and trying new columns) and saving time compared to trying all possible configurations blindly.
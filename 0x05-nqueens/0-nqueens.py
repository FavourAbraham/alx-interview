#!/usr/bin/python3
"""0x05. N Queens"""
import sys


def is_safe(row, col, queens):
    """
    Checks if postion is have no other queens in the same column or diagonal.
    """
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(row, queens, solutions):
    """
    Place queens row by row, and check if the position is safe.
    """
    N = len(queens)
    if row == N:
        solutions.append(queens[:])
        return
    for col in range(N):
        if is_safe(row, col, queens):
            queens[row] = col
            solve_nqueens(row + 1, queens, solutions)
            queens[row] = -1  # Backtrack


def n_queens(N):
    """Start the solution process"""
    queens = [-1] * N
    solutions = []
    solve_nqueens(0, queens, solutions)
    return solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
solutions = n_queens(n)
for elem in solutions:
    for pos in range(len(elem)):
        elem[pos] = [pos, elem[pos]]

for line in solutions:
    print(line)

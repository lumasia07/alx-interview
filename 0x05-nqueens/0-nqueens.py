#!/usr/bin/python3
"""Solve for N queens"""
import sys


def is_safe(board, row, col, N):
    """Saftey checks"""
    for i in range(col):
        if board[i] == row:
            return False
        if abs(board[i] - row) == abs(i - col):
            return False
    return True


def solve_nqueens(N, col, board, solutions):
    """Backtracking"""
    if col == N:
        solutions.append(board[:])
        return
    for row in range(N):
        if is_safe(board, row, col, N):
            board[col] = row
            solve_nqueens(N, col + 1, board, solutions)


def print_solutions(solutions):
    """Print all solutions"""
    for solution in solutions:
        result = []
        for col, row in enumerate(solution):
            result.append([col, row])
        print(result)


def main():
    """CLI logs"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N, 0, [-1] * N, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

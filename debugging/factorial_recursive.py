#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the first command-line argument, convert it to int, and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)

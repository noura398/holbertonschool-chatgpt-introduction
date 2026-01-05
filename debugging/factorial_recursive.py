#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculates the factorial of a number using recursion.

    Function Description:
    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. This function computes
    the factorial value recursively.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Convert command-line argument to integer
f = factorial(int(sys.argv[1]))

# Print the result
print(f)

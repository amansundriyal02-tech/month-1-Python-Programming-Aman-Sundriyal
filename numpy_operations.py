"""Practice NumPy arrays, arithmetic operations, and broadcasting."""

import numpy as np


def demonstrate_numpy():
    # Creating a one-dimensional NumPy array
    temperatures = np.array([24, 26, 28, 30, 32])
    print("\nOriginal array:", temperatures)

    # Array operations
    print("Add 2 to every value:", temperatures + 2)
    print("Multiply every value by 2:", temperatures * 2)
    print("Square every value:", temperatures ** 2)
    print("Mean:", np.mean(temperatures))
    print("Minimum:", np.min(temperatures))
    print("Maximum:", np.max(temperatures))

    # Two-dimensional array
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2D array:\n", matrix)
    print("Column sums:", np.sum(matrix, axis=0))

    # Broadcasting: add one value to every array element
    print("Broadcasting (matrix + 10):\n", matrix + 10)

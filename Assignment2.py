import unittest

# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) == 0:
        return (None, None)

    if len(numbers) == 1:
        return (numbers[0], None)

    max1 = max(numbers)
    remaining = [n for n in numbers if n != max1]

    if not remaining:  # all values identical
        return (max1, max1)

    max2 = max(remaining)
    return (max1, max2)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(list(set(numbers)))

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    # zip(*matrix) transposes rows/columns
    return [list(row) for row in zip(*matrix)]

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be the same length.")
    return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    # matrix1: A x B, matrix2: B x C → result: A x C
    rows_A = len(matrix1)
    cols_A = len(matrix1[0])
    rows_B = len(matrix2)
    cols_B = len(matrix2[0])

    if cols_A != rows_B:
        raise ValueError("Number of columns of matrix1 must equal rows of matrix2.")

    # initialize result with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # multiply
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
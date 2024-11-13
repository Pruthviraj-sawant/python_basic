import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# 3D array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Array of zeros
arr_zeros = np.zeros((2, 3))

# Array of ones
arr_ones = np.ones((2, 3))

# Array with random values
arr_random = np.random.rand(3, 3)

# Array with a range of numbers
arr_range = np.arange(0, 10, 2)

# Array with evenly spaced numbers
arr_linspace = np.linspace(0, 1, 5)  # 5 numbers between 0 and 1

print(arr_1d, arr_2d, arr_3d, arr_zeros, arr_ones, arr_random, arr_range, arr_linspace, sep='\n\n')

import numpy as np

# dtype = data type
'''
NumPy array has a dtype parameter used to specify the data type of array elements.
This is important for memory management and performance.
Create a NumPy array with a specific dtype.
By default, dtype takes the float data type.
'''
arr = np.array([1, 2, 3], dtype=float)
print(arr)  # [1. 2. 3.]    

arr1 = np.array([1, 2, 3], dtype=bool)
print(arr1)  # [ True  True  True] 

arr2 = np.array([1, 2, 3], dtype=complex)
print(arr2)  # [1.+0.j 2.+0.j 3.+0.j]

# np.arange
arr3 = np.arange(1, 11)
print(arr3)  # [ 1  2  3  4  5  6  7  8  9 10]  

arr4 = np.arange(1, 11, 2)
print(arr4)  # [ 1  3  5  7  9]


# with reshape
arr5 = np.arange(1, 11).reshape(5, 2)  # Reshape the array into 5 rows and 2 columns.
print(arr5)
"""
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]
"""

# with reshape
arr51 = np.arange(16).reshape(2,2,2, 2)  # Reshape the array into 5 rows and 2 columns.
print(arr51)
'''
[[[[ 0  1]
   [ 2  3]]

  [[ 4  5]
   [ 6  7]]]


 [[[ 8  9]
   [10 11]]

  [[12 13]
   [14 15]]]]
'''
arr6 = np.arange(1, 11).reshape(2, 5)  # Reshape the array into 2 rows and 5 columns.
print(arr6)

'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''

arr7 = np.arange(1, 13).reshape(3, 4) # Reshape the array into 3 rows and 4 columns.
print(arr7)

'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''

# Create arrays using np.ones() and np.zeros().
arr8 = np.ones((3, 4))  # create a 3x4 array of ones
print(arr8)
'''
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''

arr9 = np.zeros((3, 4)) # Create a 3x4 array filled with zeros.
print(arr9)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''

# np.random
arr10 = np.random.random((3, 4)) # Create a 3x4 array of random numbers.
'''
[[0.74415419 0.909403   0.82916525 0.91924748]
 [0.73743092 0.64315257 0.34056828 0.10536294]
 [0.75282614 0.04729358 0.93151953 0.90131202]]
'''

# np.linspace() creates evenly spaced values where the distance between two points is the same.
arr11 = np.linspace(-10, 10, 10) # Create an array of 10 evenly spaced numbers between -10 and 10.
print(arr11)  # [-10.  -7.77777778  -5.55555556  -3.33333333  -1.11111111   1.11111111   3.33333333   5.55555556   7.77777778  10.]

# np.identity() creates an identity matrix.
# An identity matrix is a square matrix with ones on the main diagonal and zeros elsewhere.
arr12 = np.identity(3)  # Create a 3x3 identity matrix.
print(arr12)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''


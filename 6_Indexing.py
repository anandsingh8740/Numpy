# Indexing 
import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)

print(a1)  # [0 1 2 3 4 5 6 7 8 9]
print(a2)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print(a3)
'''
 [[[0 1]
   [2 3]]

  [[4 5]
   [6 7]]]
'''

print(a1[-1])  # 9  # Last element
print(a1[0])   # 0  # First element

print(a2)
'''
[[ 0  1  2  3]
 [ 4  5  6-> I want (6)  7]
 [ 8  9 10 11]]
'''
# (Check row index, check column index) = [1 (row index), 2 (column index)]
print(a2[1, 2])  # 6

# 11 -> row index = 2, column index = 3
print(a2[2,3])  # 11
print(a2[1,0])  # 4

# 3D array
print("3D array ->")
print(a3)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''

# To access the value 5: -> row index = 1, column index = 0, depth index = 1
# In a 3D array:
# - 3D contains multiple 2D arrays
# - 2D contains multiple 1D arrays
# - 1D contains scalar values

# First, check how many 2D arrays are inside the 3D array -> 2 (index 0 and 1)
# Then, check row index = 1 -> [[4, 5], [6, 7]]
# Next, check column index = 0 -> [4, 5]
# Finally, check depth index = 1 -> 5

# 3D = 2, 2D = 2, 1D = 2
# print(a3[which 2D array it exists in, then access 5 using row and column index as we do in 2D arrays])
print(a3[1, 0, 1])  # 5 # [1(2D), 0(row), 1(depth)] 

# we want to found 2  
print(a3[0,1,0])  # 2

print(a3[0,0,0]) # 0

print(a3[1,1,0])  # 6

'''
Similarly, while indexing a 4D array, first check in which 4D array the 3D array exists,
then check in which 3D array the 2D array exists,
then check in which 2D array the 1D array exists,
and finally check where the scalar value exists in the 1D array.
'''


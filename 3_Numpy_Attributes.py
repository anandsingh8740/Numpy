# Array Attributes
import numpy as np


a1 = np.arange(10)
a2 = np.arange(12, dtype=float).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)

print(a1) # [0 1 2 3 4 5 6 7 8 9]
print(a2) 
'''
[[ 0.  1.  2.  3.]
 [ 4.  5.  6.  7.]
 [ 8.  9. 10. 11.]]
'''
print(a3) 
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''

# ndim -> number of dimensions
print(a1.ndim)  # 1
print(a2.ndim)  # 2
print(a3.ndim)  # 3 


# shape -> dimensions of the array
print(a1.shape)  # (10,)

print(a2.shape)  # (3, 4)
print(a3.shape)  # (2, 2, 2) # There are 2, 2D arrays, of shape (2, 2)
print(a3)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''

# size -> number of elements in the array
print(a3.size)  # 8
print(a2.size)  # 12

# itemsize -> size of each element in bytes
print(a3.itemsize)  # 8 (since the default dtype is int64, which takes 8 bytes)
print(a2.itemsize)  # 8 (since the dtype is float64, which takes 8 bytes)
print(a1.itemsize)  # 8 (since the default dtype is int64, which takes 8 bytes) 

# dtype -> data type of the elements in the array
print(a1.dtype) # int64
print(a2.dtype) # float64
print(a3.dtype) # int64

############ Changing Data Type ############
print("############ Changing Data Type ############")
print(a1)  # [0 1 2 3 4 5 6 7 8 9]
print(a1.dtype)  # int64
ast1= a1.astype(np.int32)  
print(ast1)  # [0 1 2 3 4 5 6 7 8 9]
print(ast1.dtype)  # int32
# astype() -> method to change the data type of the array
# Indexing 

import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)

# Slicing -> We can slice the array using the colon operator (:).
print("slicing ->")

print(a1)  # [0 1 2 3 4 5 6 7 8 9]

print(a1[2:5]) # [2 3 4] -> start index = 2, end index = 5 (exclusive)

print(a1[2:5:2]) # [2 4] -> start index = 2, end index = 5 (exclusive), step = 2

print(a2)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# I want the first row of a2.
print(a2[0])  # [0 1 2 3]
print(a2[0, :])  # [0 1 2 3] -> first row, all columns

# I want the 3rd column of a2.
# To get the 3rd column, we need all the rows.
print(a2[:, 2]) # [ 2  6 10]  # [all row(:), col(2)]

'''
I want 
5, 6
9, 10
'''

print(a2[1:, 1:3])   # a2[1 onwards :, 1 onwards :3 (3 not included)]
'''
[[ 5  6]
 [ 9 10]]
'''

'''
[[ 0->  1  2  3->]
 [ 4  5  6  7]
 [ 8->  9 10 11->]]
'''
 
# a2[(all rows required (0,8) :, all columns required :,
# rows should be alternate with a step of 2,
# columns will also take a jump of 2 :)]
print(a2[::2,::3]) 

'''
[[ 0  3]
 [ 8 11]]
'''
# Important: Practice these topics.
# Find 1, 3, 9, and 11.
# : -> selects all rows
# ::2 -> selects alternate rows
print(a2[: : 2, 1::2 ])  # a2[(: : 2)->row, (1::2) -> column ]

'''
[[ 1  3]
 [ 9 11]]
'''

# I want 4 and 7.
print(a2[1,::3]) # [4 7]
# I want 1 2 3 5 6 7
print(a2[0:2])
'''
[[0 1 2 3]
 [4 5 6 7]]
'''
print(a2[0:2, 1:])

'''
[[1 2 3]
[5 6 7]]
'''
print(a2[0:2, 1::2])

'''
[[1 3]
 [5 7]]
'''
print("3D -> Array")
print(a3)

'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
print("reshape")
a3 = np.arange(27).reshape(3,3,3)
print(a3)

'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''

# This NumPy array consists of 3 2D arrays.
print(a3[1])

'''
[[ 9 10 11]
 [12 13 14]
 [15 16 17]]
'''

print(a3[::2])  # [Select all elements, then select the alternate ones]
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''

# Print the 2nd row of the 1st 2D array -> [3, 4, 5]
print(a3[0, 1, :])  # [1st 2D array, 2nd row, all columns]  # [3 4 5]

# I want the middle column of the 2nd NumPy array.
print(a3[1,:,1]) # [10 13 16] 

# 22,23,25,26
print(a3[2,1:,1:])  # (a3[2nd 2D array, 1st row onwards -> select everything after 1,
# 1st column onwards -> select everything])
# 1: -> means select everything from index 1 onwards.

'''
[[22 23]
 [25 26]]
'''

# I want 0 2    18 20
print(a3[::2,0, ::2])   # a3[::2] -> used to select alternate arrays.
'''
[[ 0  2]
    [18 20]]
'''
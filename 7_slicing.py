# Indexing 

import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)

# slicing -> we can slice the array using the colon operator (:)
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

# I want first row of a2
print(a2[0])  # [0 1 2 3]
print(a2[0, :])  # [0 1 2 3] -> first row, all columns

# I want 3rd column of a2
# agar hame 3rd column chahiye to row koin sa chahiye-> hame sare rows chahiye

print(a2[:, 2]) # [ 2  6 10]  # [all row(:), col(2)]

'''
I want 
5, 6
9, 10
'''

print(a2[1:, 1:3])   # a2[1 ke onward:, 1 onwards :3(not include)]
'''
[[ 5  6]
 [ 9 10]]
'''

'''
[[ 0->  1  2  3->]
 [ 4  5  6  7]
 [ 8->  9 10 11->]]
'''
print(a2[::2,::3])  # (a2[(total row chahiye(0,8) :, charo column chahiye :, rows alternate chaiye 2(sare rows ayege alternat wal) column 2 ,2 ka jump lega, :])

'''
[[ 0  3]
 [ 8 11]]
'''
# Imp:- practice on this topics
# find out 1, 3, 9, 11  # : -> all the row : : 2 -> means we want alternate row
print(a2[: : 2, 1::2 ])  # a2[(: : 2)->row, (1::2) -> column ]

'''
[[ 1  3]
 [ 9 11]]
'''

# I want 4, 7
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

# This numpy array consist of 3, 2D arrays
print(a3[1])

'''
[[ 9 10 11]
 [12 13 14]
 [15 16 17]]
'''

print(a3[::2])  # [sabko nikal lo , aur phir alternate wale ko nikal lo]

'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''

# 1st 2d array ka hai uska 2nd row print kara kar do -> [3, 4, 5]
print(a3[0, 1, :])  # [1st 2D array, 2nd row, all the columns]  # [3 4 5]


# 2nd wale numpy ka bich wala column chahiye
print(a3[1,:,1]) # [10 13 16] 

# 22,23,25,26
print(a3[2,1:,1:])  # (a3[2nd D, 1->row:(onwards)->sabkuch chaiye age ka, 1st column onward : ->sabkuch]) -- 1:-> means 1 se agae sabkuch

'''
[[22 23]
 [25 26]]
'''

# I want 0 2    18 20
print(a3[::2,0, ::2])   # a3[::2 -> we can find out alternate array]

'''
[[ 0  2]
    [18 20]]
'''
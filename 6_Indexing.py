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
# (check row index, check column index) = [1(6-row index), 2(6->column index)]
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
 # I want 5 -> row index = 1, column index = 0, depth index = 1
# 3D make always 2D and 2D make always 1D and 1D make always scalar
# first check inside 3D how many 2D are there -> 2 (0 and 1) -> check row index = 1 -> [[4 5], [6 7]] -> check column index = 0 -> [4, 5] -> check depth index = 1 -> 5

# 3D = 2, 2D = 2, 1D = 2
# print(a3[koin se wale array me 2D me exist karta hai, 2nd wale 2D me, aur ab 5 ko jaise nikalege jaise 2D se nikalate the row and column index se])
print(a3[1, 0, 1])  # 5 # [1(2D), 0(row), 1(depth)] 

# we want to found 2  
print(a3[0,1,0])  # 2

print(a3[0,0,0]) # 0

print(a3[1,1,0])  # 6

# similarly 4 D array me indexing karte time 4th wale array me check karna hai ki 3D kaha exist karta hai, 3D me check karna hai ki 2D kaha exist karta hai, 2D me check karna hai ki 1D kaha exist karta hai, aur 1D me check karna hai ki scalar kaha exist karta hai


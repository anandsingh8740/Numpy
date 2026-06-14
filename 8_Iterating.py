# Iterating
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

for i in a1:
    print(i)
    
'''
0
1
2
3
4
5
6
7
8
9
'''

for i in a2:
    print(i)
'''
[0 1 2 3]
[4 5 6 7]
[ 8  9 10 11]
'''

for i in a3:
    print(i)
'''
[[0 1]
 [2 3]]
[[4 5]
 [6 7]]
'''

for i in np.nditer(a3):
    print(i)
    
'''
0
1
2
3
4
5
6
7
'''
####################################
# Reshaping

# reshape

# Transpose -> converts rows into columns.
print("Transpose")
print(a2)

'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print(np.transpose(a2))

'''
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''

# Another syntax for transpose -> gives the same output.
print(a2.T)
'''
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''

# ravel -> converts any dimensional array into a 1D array.
print("reval")

print(a2)

'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print(a2.ravel())  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a3.ravel())  # [0 1 2 3 4 5 6 7]


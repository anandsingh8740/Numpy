# Splitting
import numpy as np

# horizontal Splitting
a4 = np.arange(12).reshape(3, 4)
a5 = np.arange(12, 24).reshape(3,4)
print(a4)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

print(np.hsplit(a4, 2))  # I want to divide a4 into 2 parts.
'''
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
'''

print(np.hsplit(a4, 4))  # I want to divide a4 into 4 parts.
'''
[array([[0],
       [4],
       [8]]), array([[1],
       [5],
       [9]]), array([[ 2],
       [ 6],
       [10]]), array([[ 3],
       [ 7],
       [11]])]
'''

# print(np.hsplit(a4, 5))  # gives error -> ValueError: array split does not result in an equal division

# vertical splitting
print("# vertical splitting")
print(a5)

'''
[[12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''

print(np.vsplit(a5, 3))
# [array([[12, 13, 14, 15]]), array([[16, 17, 18, 19]]), array([[20, 21, 22, 23]])]

# print(np.vsplit(a5, 2)) # ValueError: array split does not result in an equal division
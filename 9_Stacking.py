# Stacking
import numpy as np

# horizontal stacking
a4 = np.arange(12).reshape(3, 4)
a5 = np.arange(12, 24).reshape(3,4)
print(a4)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

print(a5)
'''
[[12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''

# horizontal stacking
print(np.hstack((a4, a5)))
'''
[[ 0  1  2  3 12 13 14 15]
 [ 4  5  6  7 16 17 18 19]
 [ 8  9 10 11 20 21 22 23]]
'''

print(np.hstack((a4, a5, a4)))

'''
[[ 0  1  2  3 12 13 14 15  0  1  2  3]
 [ 4  5  6  7 16 17 18 19  4  5  6  7]
 [ 8  9 10 11 20 21 22 23  8  9 10 11]]
'''
# Vertical stacking
print(np.vstack((a4, a5)))
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''


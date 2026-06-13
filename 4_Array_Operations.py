# Array Operations in NumPy 
import numpy as np

a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

print(a1)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print(a2)

'''
[[12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''
print("Scalar operations ->")
# Scalar operations -> single value is applied to all elements of the array
# arithmetic operations
print(a1*2)   # (a1-> matrix, 2-> scalar)
'''
[[ 0  2  4  6]
 [ 8 10 12 14]
 [16 18 20 22]]
'''

print("Relational operations ->")
print(a1 > 5)   # (a1-> matrix, 5-> scalar) # or a2== 15 like that comparison can be done

'''
[[False False False False]
 [False False  True  True]
 [ True  True  True  True]]
'''
print("Vectorized operations ->")
# Vectorized operations -> jab do numpy arrays ke uper ham operations perform karte hai to wo element wise perform hota hai, isko vectorized operations kehte hai
# Arithmetic operations
print(a1 + a2)   # (a1-> matrix, a2-> matrix) # dono matrix ke corresponding elements ka sum nikalta hai

# we can do all the operators like addition, subtraction, multiplication, division, etc. with two arrays of the same shape 
'''
[[12 14 16 18]
 [20 22 24 26]
 [28 30 32 34]]
'''

print(a1**a2)

'''
[[                   0                    1                16384
              14348907]
 [          4294967296         762939453125      101559956668416
     11398895185373143]
 [ 1152921504606846976 -1261475310744950487  1864712049423024128
   6839173302027254275]]
'''

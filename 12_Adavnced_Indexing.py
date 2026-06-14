# Advanced Indexing
import numpy as np

# Normal Indexing and slicing 
print("Normal Indexing")
a = np.arange(12).reshape(4,3)
print(a)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

print(a[1,2])  # 5

print(a[1:3, 1:3])
'''
[[4 5]
 [7 8]]
'''

# Fancy Indexing
print("Fancy Indexing")

print(a)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

print(a[::2])
'''
[[0 1 2]
 [6 7 8]]
'''
# I want the 1st, 3rd, and 4th rows — we can easily get the values using normal indexing.
# Fancy Indexing -> We pass a list inside the same square brackets.
# In that list, we provide the index positions of the rows we want.

print(a[[0, 2,3]]) # I want [1st row, 3rd row, 4th row] — this way we can provide the index.
'''
[[ 0  1  2]
 [ 6  7  8]
 [ 9 10 11]]
'''

a1 = np.arange(24).reshape(6,4)
print(a1)

'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''
# I want the 1st, 3rd, 4th, and 6th rows.
print(a1[[0,2,3,5]])
'''
[[ 0  1  2  3]
 [ 8  9 10 11]
 [12 13 14 15]
 [20 21 22 23]]
'''
# I want the 1st, 2nd, and 3rd columns.
print(a1[:,[[0,2,3]]])  # [:,-> all rows, [[column-> 0, 2,3rd -> column]]

'''
[[[ 0  2  3]]

 [[ 4  6  7]]

 [[ 8 10 11]]

 [[12 14 15]]

 [[16 18 19]]

 [[20 22 23]]]
'''

################################################
# Boolean Indexing
print(" Boolean Indexing")
a = np.random.randint(1,100,24).reshape(6,4)
print(a)

'''
[[40 25 51 52]
 [60 57 59 17]
 [ 3 10 75 48]
 [66 41 58 89]
 [69 19 60  7]
 [56 44 69 71]]
'''

# Find all numbers greater than 50.
print(a>50)

'''
[[False False False  True]
 [ True False False  True]
 [False False False False]
 [ True False False False]
 [False  True False  True]
 [ True False  True  True]]
'''
print(a[a>50]) # Only get those numbers which are greater than 50.
# [77 54 78 93 83 82 62 95]

# find out even numbers
print(a%2==0)
'''
[[False  True False False]
 [False False  True  True]
 [False False False  True]
 [False False False False]
 [False  True  True  True]
 [False False  True  True]]
'''

# another format
print(a[a%2==0]) # [16 38 68 64 58 36]

# Find all numbers greater than 50 and that are even.
print((a>50) & (a%2==0))
'''
[[False False False False]
 [False False False False]
 [False False  True False]
 [False False False False]
 [False False False False]
 [ True False  True  True]]
'''
print(a[(a>50) & (a%2==0)]) # [58 66 72 60 58 70 80]


# Find all numbers that are not divisible by 7.
print(a[~(a%7 == 0)]) # [58  8  3 45 75 58 30 55 23 96 95 87 17 31 3 43 90 74 64]

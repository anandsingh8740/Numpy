# Array Functions
import numpy as np

a1 = np.random.random((3, 4))
a1 = np.round(a1*100)
print(a1)
'''
[[40. 36. 13. 25.]
 [39. 94. 46. 33.]
 [42. 39. 70. 80.]]
'''

# max/min/sum/prod
print("max/min/sum/prod ->")

print(np.max(a1))   # 89.0
print(np.min(a1))   # 13.0
print(np.sum(a1))   # 517.0
print(np.prod(a1))  # 1.2345678901234567e+19

###### Imp -> 0-> col, and 1 ->row
print("# I want every row minimum")
print("###### Imp -> 0-> col, and 1 ->row")
# I want every row minimum
print(np.min(a1, axis=1)) # [35. 38.  6.]
print(np.max(a1, axis=1)) # [95. 83. 92.]

# Column wise maximum item
print(np.max(a1, axis=0)) # [46. 95. 93. 32.]
print(np.min(a1, axis=0)) # [35. 38.  6. 32.]
print(np.sum(a1, axis=0)) # [126. 162. 165. 153.]
print(np.prod(a1, axis=0)) # [ 72380.  84688. 121992. 127200.]

# mean/median/std/var
print("mean/median/std/var ->")
print(np.mean(a1))   # 48.0
print(np.mean(a1, axis=0))   # [46.66666667 50.         37.33333333 50.        ]
print(np.mean(a1, axis=1))   # [53.25 37.25 47.5 ]

print(np.median(a1))   # 39.0
print(np.median(a1, axis=0))   # [40. 39. 46. 32.]

print(np.std(a1))   # 26.798113532278517
print(np.var(a1))   # 718.138888888889


# trigonometric functions
print("trigonometric functions ->")
print(np.sin(a1))
'''
[[-0.521551   -0.98803162 -0.99177885 -0.95375265]
 [ 0.76255845  0.27090579  0.85090352 -0.17607562]
 [ 0.39592515  0.90178835  0.25382336 -0.95375265]]
'''
print("code for cos")
print(np.cos(a1))
'''
[[ 0.85322011  0.15425145 -0.12796369  0.30059254]
 [ 0.64691932 -0.96260587  0.52532199 -0.98437664]
 [-0.91828279 -0.43217794 -0.96725059  0.30059254]]
'''
# dot product
'''
3 4   4  3
|  |___| |  = equal then dot product can be performed
|________|  = resultant matrix will be of shape (3, 3)

(3, 5) and (3, 5) -> dot product cannot be performed because (1, 5(equal)), (3(equal), 5(com)) -> not equal
'''

print("dot product ->")
a2 = np.arange(12).reshape(3, 4)
a3= np.arange(12, 24).reshape(4, 3)
print(a2)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

print(a3)
'''
[[12 13 14]
 [15 16 17]
 [18 19 20]
 [21 22 23]]
'''

print("dot")
print(np.dot(a2, a3))

'''
[[114 120 126]
 [378 400 422]
 [642 680 718]]
'''

# log and exponents
print("log and exponents ->")
print(np.log(a1))
'''
[[4.57471098 3.76120012 4.04305127 3.49650756]
 [4.31748811 3.76120012 4.56434819 4.48863637]
 [4.24849524 4.07753744 3.55534806 4.2341065 ]]
'''
print(np.exp(a1))
'''
[[1.33833472e+42 4.72783947e+18 5.68572000e+24 2.14643580e+14]
 [3.73324200e+32 4.72783947e+18 4.92345829e+41 4.48961282e+38]
 [2.51543867e+30 4.20121040e+25 1.58601345e+15 9.25378173e+29]]
'''

# round and floor/ceil
print("round and floor/ceil ->")
print(np.random.random((3, 2)))
'''
[[0.96354766 0.52043423]
 [0.84374853 0.88254651]
 [0.04599726 0.03593547]]
'''
print(np.random.random((3, 2))*100)
'''
[[38.48107617 82.97940362]
 [81.62817704 36.32100676]
 [56.82368473 89.58743267]]
'''
# floor -> rounds down to the nearest lower value
# ceil -> rounds up to the nearest higher value
print(np.round(np.random.random((2, 3))*100))
'''
[[88. 31. 30.]
 [ 9. 18.  1.]]
'''

print(np.floor(np.random.random((2, 3))*100))
'''
[[29. 44. 28.]
 [31. 92.  8.]]
'''
# Ceil -> rounds up to the nearest higher value
# Example:
# ceil(6.1) = 7
# ceil(-6.1) = -6
# ceil(6.9) = 7
# ceil(-6.9) = -6
print(np.ceil(np.random.random((2, 3))*100))
'''
[[ 3. 51. 99.]
 [55.  5. 57.]]
'''
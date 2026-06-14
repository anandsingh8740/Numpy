# Broadcasting -IMP TOPICS
'''
The term broadcasting describes how NumPy treats arrays with different 
shapes during arithmetic operations.

The smaller array is "broadcast" across the larger array so that they 
have compatible shapes.

'''
import numpy as np

# same shape
a= np.arange(6).reshape(2,3)
b = np.arange(6, 12).reshape(2,3)

print(a)
'''
[[0 1 2]
 [3 4 5]]
'''
print(b)

'''
[[ 6  7  8]
 [ 9 10 11]]
'''
print("a+b")
print(a + b)
'''
[[ 6  8 10]
 [12 14 16]]
'''
# diff shape
a1 = np.arange(6).reshape(2,3)
b1 = np.arange(3).reshape(1,3)

print(a1)
'''
[[0 1 2]
 [3 4 5]]
'''

print(b1)
'''
[[0 1 2]]
'''
print(a1+b1)
'''
[[0 2 4]
 [3 5 7]]
'''
'''
Broadcasting Rules:-
1. Make the two arrays have the same number of dimensions.
▶️ If the numbers of dimensions of the two arrays are different, add new
    dimensions with size  1 to the head of the array with the smaller dimension.
    
2. Make each dimension of the two arrays the same size.
▶️ If the sizes of each dimension of the two arrays do not match, dimension
    with size 1 are stretched to the size of the other array.
    # for making same dimension
    Example:- (3,2) , (3,) -> make from our end ----->(1, 3)  -> add 1
    Example:- (3,3,3) -> 3d and (3,) -> 1D make from aur end ---> (1,1,3)
    
▶️ If the sizes of each dimension whose size is not 1 in either of the 
    two arrays, it can not be broadcasted, and an error is raised.
    
    Example:- (3,3) , (3,) -> make from our end ----->(1, 3)  -> add 1
    (3,3) and (1,3) -> dimension wise not same, make (1--->3,3) -> (3,3)
    Example 2:- (4,3) and (3) -> (4,3) and (1,3) -> (4,3) and (1--->4, 3) -> both are same -> broadcasting will be follow
    
'''

# More examples
a = np.arange(12).reshape(4,3)
b = np.arange(3)

print(a)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''
print(b)
'''
[0 1 2]
'''

print(a + b)
'''
[[ 0  2  4]
 [ 3  5  7]
 [ 6  8 10]
 [ 9 11 13]]
'''

a = np.arange(12).reshape(3,4)
b = np.arange(3)

#print(a+b)  # -> (3,4), (3) -> (3,4), (1,3) -> (3,4), (1-->3, 3) => not possible broadcasting
'''
print(a+b)
          ~^~
ValueError: operands could not be broadcast together with shapes (3,4) (3,) 
'''

a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3, 1)
# (1,2)->2D, (3, 1)->2D => (1-->3,3), (3,1-->3) => broadcasting possible
print(a) # [[0 1 2]]
print(b)
'''
[[0]
 [1]
 [2]]
'''
print(a+b)
'''
[[0 1 2]
 [1 2 3]
 [2 3 4]]
'''

a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4, 1)

# (1,3)->2D, (4,1)->2D  => (1-->4,3),(4, 1--->3) => (4,3), (4,3) => possible
print(a+b)

a = np.array([1])
# shape -> (1,1)
b = np.arange(4).reshape(2,2)
# shape -> (2,2)
# (2,2) , (1) => (2,2), (1,2)->(2,1)->(2,2) , (2,2), (2,2)
print(a) # [1]
print(b)
'''
[[0 1]
 [2 3]]
'''
print("a+b")
print(a+b)
'''
[[1 2]
 [3 4]]
'''

a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4, 3)
print(a) 
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print(b)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''
print("addition")
# (3,3), (4,3) => 1 is not present in both places, so we cannot expand dimensions.
# Therefore, broadcasting is not possible.
# print(a+b)  # ValueError: operands could not be broadcast together with shapes (3,4) (4,3)

a = np.arange(16).reshape(4,4)
b = np.arange(4).reshape(2, 2)

print(a)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
print(b)
'''
[[0 1]
 [2 3]]
'''
# (2,2) != (4,4)
# print(a+b) # ValueError: operands could not be broadcast together with shapes (4,4) (2,2) 

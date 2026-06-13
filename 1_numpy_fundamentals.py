'''
# Question :- What is NumPy?

Ans:-NumPy is the fundamental package for scientific computing in Python.
It is a Python library that provides a multidimensional array object,
various derived objects (such as masked arrays and matrices), and an 
assortment of routines for fast operations on arrays, including mathematical, 
logical, shape manipulation, sorting, selecting, I/O, discrete Fourier 
transforms, basic linear algebra, basic statistical operations, random 
simulation and much more.

At the core of the NumPy package, is the ndarray object. This encapsulates
n-dimensional arrays of homogeneous data types.
'''

'''
# Question :- NumPy Arrays Vs Python Sequences

1. NumPy arrays have a fixed size at creation, unlike Python lists 
(which can grow dynamically). Changing the size of an ndarray will 
create a new array and delete the original.

2. The elements in a NumPy array are all required to be of the same data
type, and thus will be the same size in memory.

3. NumPy arrays facilitate advanced mathematical and other types of 
operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

4. A growing plethora of scientific and mathematical Python-based packages
are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.
'''

# Creating NumPy Arrays

# np.array
# first import the numpy
import numpy as np
# 1D array -> Vector
a = np.array([1, 2, 3])
print(a)
print(type(a))

'''
[1 2 3]
<class 'numpy.ndarray'>
'''

# 2D and 3D => 2d like matrix
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

'''
[[1 2 3]
 [4 5 6]]
'''

# 3D array -> Tensor
c = np.array([[[1,2], [3,4]],[[5,6], [7,8]]])
print(c)

'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''
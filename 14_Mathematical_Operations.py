# Mathematical Operations in NumPy
import numpy as np

# Working with mathematical formulas.

a = np.arange(10)
print(a)  # [0 1 2 3 4 5 6 7 8 9]

print(np.sum(a)) # 45

print(np.sin(a))
'''
[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
 -0.2794155   0.6569866   0.98935825  0.41211849]
'''

# sigmoid  -> S(x) = 1/(1+e^-x) => Sigmoid value between 0 to 1
print("############ sigmoid ###################")
def sigmoid(array):
    return 1/(1+np.exp(-(array)))
a = np.arange(10)

print(sigmoid(a))
'''
0.5        0.73105858 0.88079708 0.95257413 0.98201379 0.99330715
0.99752738 0.99908895 0.99966465 0.99987661]

'''
# mean squared error =>
print("##### mean squared error ###########")

actual = np.random.randint(1,20,25)
predicted = np.random.randint(1,50,25)

print(actual)
# [18 10 17 19  2 18  1  3  1 17  4 17  6  6  8 19  3 16  8  1 14  4 16 15 17]
print(predicted)
# [26  7 37 21 34 49 36 14 19 45 38  2 38  2 23  7 42 29 41 45 35 46 13 20 48]
print(actual - predicted) 
# [ -8   3 -20  -2 -32 -31 -35 -11 -18 -28 -34  15 -32   4 -15  12 -39 -13 -33 -44 -21 -42   3  -5 -31]
def mse(actual, predicted):
    return np.mean((actual - predicted)**2)
    
print(mse(actual, predicted)) # 624.84

print((actual- predicted)**2)
# [  36  289    9    1   25 1024  961    0  529   16    4    4    1  576 81  100    4   25   81  900  625  784  729  625  729]

print(np.mean(actual- predicted)**2) # 186.04960000000003

# H.W -> Binary cross entropy
 
# categorical cross entropy


# Working with missing values -> np.nan
# NaN means missing value
print("#### Working with missing value -> np.nan ###")
a = np.array([1,2,3,4, np.nan, 6])
print(a)  # [ 1.  2.  3.  4. nan  6.]

# How can I remove missing values?
# Evaluate without missing values
# isnan() -> checks whether a value is missing or not

print(np.isnan(a)) # [False False False False  True False]

print(a[np.isnan(a)]) # [nan]

print(a[~np.isnan(a)]) # [1. 2. 3. 4. 6.]


# Numpy array vs Python lists
import numpy as np
# speed
# list
a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]

c = []
import time
start = time.time()   # measure the current time
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time() - start) # 1.7499377727508545

# numpy
print("Numpy")
a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start = time.time()   # measure the current time
c = a + b
print(time.time() - start) # 0.15776371955871582

# Imp :- Numpy is more faster then python list.
# Numpy use c type array -> it is a static array and it is a referential array

# Memory
a = [i for i in range(10000000)]
import sys
print(sys.getsizeof(a)) # 89095160

a = np.arange(10000000)
print(sys.getsizeof(a)) # 80000112

a = np.arange(10000000, dtype=np.int32) # using int32 bit the storage will be half
print(sys.getsizeof(a)) # 40000112

a = np.arange(10000000, dtype=np.int16) # using int32 bit the storage will be half
print(sys.getsizeof(a)) # 20000112

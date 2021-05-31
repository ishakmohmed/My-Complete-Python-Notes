import numpy as np

array = np.array([1, 2, 3])  # can pass a matrix too
print(array)  # instance of ndarray in numpy
print(array.shape)

array = np.zeros((3, 4), dtype=int)
print(array)
array2 = np.ones((3, 4), dtype=int)
print(array2)
array3 = np.full((3, 4), 9, dtype=int)
print(array3)
array4 = np.random.random((3, 4))
print(array4)
print(array4[0, 0])

print(array4 > 0.2)
# will reprint the array and each element will be evaluated with this expression and filled with True or False

print(array4[array4 > 2])
# will return new array with values that are only greater than 0.2

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])

print(first + second)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)

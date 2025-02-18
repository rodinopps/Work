import numpy as np
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr * 2)
print(arr + 3)
print(arr ** 2)

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2 > arr)

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1])
print(arr3[:, 1])
print(arr3[0:2, 1:3])

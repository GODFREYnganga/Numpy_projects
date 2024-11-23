import numpy as np

arr = np.array([1, 2,3,4, 5])

print(arr)
print(type(arr))
print(np.__version__)

arr_2d = np.array([[1, 2,3], [4,5,6]])
print(arr_2d)

arr_3d =([[[1,2,3],[4, 5, 6]], [[1,2,3], [4,5,6]]])
print(arr_2d)

#checking number of dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


arr_nd = np.array([1,2,3,4], ndmin =5)
print(arr_nd)
print("Number of dimensional array: ", arr_nd.ndim)
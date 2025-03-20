#Arithmetic operations on single nad multidimensional

1)import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(a+b)  # 6, 8 , 10, 12
print(a%b)
output:
[ 6  8 10 12]
[1 2 3 4]

2)a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

'''print(a)
print(b)'''

print(a+b)
output:
[[1 2]
 [3 4]]
[[5 6]
 [7 8]]
[[ 6  8]
 [10 12]]

3)a = np.array([[[1,2],[3,4],[5,6]]])
b = np.array([[[5,6],[7,8],[0,9]]])

'''print(a)
print(b)'''

print(a+b)
print(a*b)
output:
[[[ 6  8]
  [10 12]
  [ 5 15]]]
[[[ 5 12]
  [21 32]
  [ 0 54]]]

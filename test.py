import numpy as np
a = np.random.randn(4, 3) # a.shape = (4, 3)
b = np.random.randn(4, 1) # b.shape = (3, 2)
c = a+b #np.dot(a,b)
# print(c.shape)


a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b
# print(c.shape)


A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True)
print(B.shape)
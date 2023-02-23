import numpy as np
np.set_printoptions(precision=3, suppress=True)

A = np.array([[1., 2.],
              [3., 4.]])
C = np.array([[5., 3., 2., 1.],
              [6., 2., 4., 5.],
              [7., 4., 1., 3.],
              [4., 3., 5., 2.]])
D = np.array([[4.],
              [2.],
              [5.],
              [1.]])

A_inv = np.linalg.inv(A)
print(A_inv)
print(np.matmul(A_inv, A))

B = np.random.rand(3, 3)
B_inv = np.linalg.inv(B)
print(np.matmul(B, B_inv))

x = np.matmul(np.linalg.inv(C), D)
print(x)
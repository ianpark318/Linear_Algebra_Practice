import numpy as np
np.set_printoptions(precision=3, suppress=True)

def Doolittle(A):
    # Square matrix
    n, m = A.shape
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(i):
                U[i, j] = U[i, j] - L[i, k] * U[k, j]
        L[i, i] = 1
        if i < n - 1:
            p = i + 1
            for j in range(p):
                L[p, j] = A[p, j]
                for k in range(j):
                    L[p, j] = L[p, j] - L[p, k] * U[k, j]
                L[p, j] = L[p, j] / U[j, j]
    return L, U


def LUSolve(A, b):
    L, U = Doolittle(A)
    n, m = L.shape
    # Ly = b
    y = np.dot(np.linalg.inv(L), b)
    # Ux = y
    x = np.dot(np.linalg.inv(U), y)
    return x


A = np.array([[5., 3., 2., 1.],
              [6., 2., 4., 5.],
              [7., 4., 1., 3.],
              [4., 3., 5., 2.]])
b = np.array([[4.],
              [2.],
              [5.],
              [1.]])

x = LUSolve(A, b)
print(x)
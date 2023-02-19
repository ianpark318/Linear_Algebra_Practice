import numpy as np

A = np.array([
    [1., 2.],
    [3., 4.]
])
B = np.array([
    [2., 2.],
    [1., 3.]
])
C = np.array([
    [4., 5., 6.],
    [7., 8., 9.]
])
v = np.array([
    [10.],
    [20.]
])
D11 = np.array([
    [1., 2.],
    [3., 4.]
])
D12 = np.array([
    [5.],
    [6.]
])
D21 = np.array([7., 7.])
D22 = np.array([8.])

print('----A+B----\n', A + B, '\n---------', sep='')
print('----A-B----\n', A - B, '\n---------', sep='')
print('----3A----\n', 3 * A, '\n---------', sep='')
print('----2v----\n', 2 * v, '\n---------', sep='')
print('----AB----\n', np.matmul(A, B), '\n---------', sep='')
print('----AC----\n', np.matmul(A, C), '\n---------', sep='')
print('----Av----\n', np.dot(A, v), '\n---------', sep='')
print('----A^2----\n', np.linalg.matrix_power(A, 2), '\n---------', sep='')
print('----A^3----\n', np.linalg.matrix_power(A, 3), '\n---------', sep='')
print('----A*B 성분별----\n', np.multiply(A, B), '\n---------', sep='')
print('----A/B----\n', A / B, '\n---------', sep='')
print('----A^2 성분별----\n', A**2, '\n---------', sep='')
print('----A.T----\n', A.T, '\n---------', sep='')
print('----v.T----\n', v.T, '\n---------', sep='')
print('----diag(1,2,3)----\n', np.diag([1, 2, 3]), '\n---------', sep='')
D = np.block([
    [D11, D12],
    [D21, D22]
])
print('----D----\n', D, '\n---------', sep='')
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])
C = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
E = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

A = np.row_stack([v1, v2, v3])
print('----A----\n', A, '\n---------', sep='')
B = np.column_stack([v1, v2, v3])
print('----B----\n', B, '\n---------', sep='')
D = np.column_stack([C, v3])
print('----D----\n', D, '\n---------', sep='')

print('E[0, 3] is', E[0, 3])
print('E[1, 2] is', E[1, 2])
print('E[0:2, 2] is', E[0:2, 2])
print('E[0:2, 2:4] is\n', E[0:2, 2:4], '\n---------', sep='')
print('E[2, :] is', E[2, :])
E[0, 0] = -1
print('E[0, 0] is', E[0, 0])

#print(D)
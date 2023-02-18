# 행렬과 벡터의 크기 출력하는 프로그램

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
v = np.array([
    [1],
    [2],
    [3]
])
w = np.array([1, 2, 3])
B = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.shape, v.shape, w.shape, B.shape)
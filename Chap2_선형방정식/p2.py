# 가우스-조단 수행하는 gauss()

import numpy as np

def printMatrix(M):
    row, col = M.shape
    Matrix = ""
    for i in range(row):
        line = "|"
        for j in range(col-1):
            line += f"{M[i, j]:.2f}\t"
        line += f"{M[i, -1]:.2f}|\n"
        Matrix += line
    print(Matrix)

def gauss(A):
    row, col = A.shape
    for i in range(row):
        maxVal = abs(A[i, i])
        maxRow = i
        for j in range(i+1, row):
            if abs(A[j, i]) > maxVal:
                maxVal = abs(A[j, i])
                maxRow = j
        for j in range(col):
            A[i, j], A[maxRow, j] = A[maxRow, j], A[i, j]   # swap elements
        #만약 i번째 열의 모든 원소가 0이면 다음 열로 넘어감
        pivot = A[i, i]
        if pivot == 0:
            continue
        A[i, :] = A[i, :] / pivot   # pivot 1로 만들어줌
        # 나머지 행들의 i번째 열 원소 0으로 만들어주기
        for j in range(row):
            if j != i:
                A[j, :] = A[j, :] - A[j, i] * A[i, :]
        printMatrix(A)  # 중간과정 보여줌

    x = A[:, -1]
    return x


# 행렬의 자료형을 float으로 선언을 해줘야 나누기 연산 등의 결과가 실수로 나옴
A = np.array([
    [2., 2., 4., 18.],
    [1., 3., 2., 13.],
    [3., 1., 3., 14.]
])

x = gauss(A)
print("Solution is", x)

# 이 프로그램의 한계점
# 불능, 부정의 해에 대해서는 결과를 내지 못함
# 좀 더 general한 프로그램 작성 해보는 것도 재밌을 것 같음
# 정수의 개수를 입력받은 다음, 해당하는 개수만큼의 정수를 입력받아 합을 계산하는 함수 calc() 작성하라.

def calc():
    n = int(input())
    sum = 0
    for i in range(n):
        num = int(input())
        sum += num
    return sum


print(f"Sum is {calc()}")
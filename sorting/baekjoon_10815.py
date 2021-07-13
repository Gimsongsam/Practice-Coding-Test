# 백준 10815번: 숫자 카드

import sys

def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 원소의 갯수와 전체 원소 입력 받기
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

# target(찾고자 하는 값)을 입력 받기
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

# print(array)
# print(target)

# 결과
for i in range(m):
    result = binary(array, target[i], 0, n-1)
    if result == None:
        print(0, end=" ")
    else:
        print(1, end=" ")

# 백준 2751: 수 정렬하기2

from sys import stdin
n = int(stdin.readline())

li = [0] * n
for i in range(n):
    li[i] = int(stdin.readline())

li.sort()

result = ""
for i in li:
    result += (str(i) + '\n')

print(result)
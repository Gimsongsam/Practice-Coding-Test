# 백준 10989번: 수 정렬하기3

import sys

n = int(input())

li = []
for i in range(10001):
    li.append(0)

for i in range(n):
    c = int(sys.stdin.readline())
    li[c] += 1 

for i in range(len(li)): # 0 ~ 10001
    for j in range(li[i]):
        sys.stdout.write(str(i))
        sys.stdout.write("\n")
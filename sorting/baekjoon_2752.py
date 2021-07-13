# 백준 2752번: 세수정렬

import sys
n = sys.stdin.readline().split()

n = list(map(int,n))
n.sort()

for i in range(len(n)):
    print(n[i], end=" ")
# 백준 10825번: 국영수

import sys
n = int(sys.stdin.readline())

l = []
for i in range(n):
    l.append(tuple(sys.stdin.readline().split()))

l.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), str(x[0])))


result = ""
for i in range(n):
    result += (l[i][0] + '\n')

print(result)
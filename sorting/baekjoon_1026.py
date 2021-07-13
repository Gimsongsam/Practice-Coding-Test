# 백준 1026번: 보물

n = int(input())

A = input().split()
A = list(map(int, A))

B = input().split()
B = list(map(int, B))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(n):
    S += A[i]*B[i]


print(S)
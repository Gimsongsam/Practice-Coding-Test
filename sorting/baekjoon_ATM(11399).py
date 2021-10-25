# 백준 11399번: ATM

n = int(input())
a = input().split()
a = list(map(int, a))
a.sort()

Num = []

for i in range(n+1):  # 0 1 2 3 4 5
    Num.append(0)
    for j in range(i):  # 0 1 2 3 4
        Num[i] += a[j]
Num.pop(0)

result = 0
for i in range(n):
    result += Num[i]
print(result)
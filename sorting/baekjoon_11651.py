# 백준 11651번: 좌표 정렬하기 2

n = int(input())

num = []
for i in range(n):
    a = input().split()
    a = list(map(int, a))
    num.append(a)

num.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    for j in range(2):
        print(num[i][j], end=" ")
    print("")
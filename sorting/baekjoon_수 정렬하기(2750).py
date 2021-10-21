# 백준 2650: 수 정렬하기

n=int(input())

s=[]

for i in range(n):
    s.append(int(input()));
s.sort()

for i in range(n):
    print(s[i])

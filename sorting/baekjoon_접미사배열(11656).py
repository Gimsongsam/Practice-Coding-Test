# 백준 11656번: 접미사 배열

s = str(input())
l = len(s)

arr = []
for i in range(l):
    arr.append(s[i:l])

arr.sort()

for i in range(len(arr)):
    print(arr[i])
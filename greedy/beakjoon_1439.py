# 백준 1439번: 뒤집기

n = input()

num = []
for i in range(len(n)):
    num.append(n[i])
num = list(map(int, num))
num.sort(reverse=True)
# print(num)

for i in range(len(num)):
    print(num[i], end="")
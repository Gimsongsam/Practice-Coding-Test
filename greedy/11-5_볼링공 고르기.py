# 볼링공 수 N개 공의 무게 1 ~ M 까지 자연수
# 공을 고르는 경우의 수

n, m = map(int, input().split())

data = list(map(int, input().split()))

count = []

result = 0
for i in range(n):
    for j in range(n):
        if (i, j) in count or (j, i) in count:
            continue
        elif data[i] != data[j]:
            result += 1
            count.append((i, j))
            
print(count)
print(result)


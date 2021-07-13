# 현재 수를 가지고 있는 단위로 만들 수 있는지 판단

n = int(input())

data = list(map(int, input().split()))

result = 1

while True:
    count = result

    for i in range(n):
        if count >= data[i]:
            if count - data[i] == 0:
                count = 0
                break
            else:
                count = count - data[i]
                continue
        else:
            continue
    if count > 0:
        break
    result += 1

print(result)
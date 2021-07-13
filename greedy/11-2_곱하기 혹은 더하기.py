s = input()

data = []
for i in range(len(s)):
    data.append(int(s[i]))

result = 0
for i in range(len(s)):
    # 현재 수가 0 이거나 곱하거나 더할 수가 0이라면 더하기
    if data[i] == 0 or result == 0:
        result += data[i]
        continue
    result *= data[i]

print(result)


t = int(input())

data = [300, 60, 10]

result = []
for i in range(len(data)):
    result.append(t // data[i])
    t = t % data[i]

if t > 0:
    print(-1)
else:
    for i in range(len(data)):
        print(result[i], end=" ")
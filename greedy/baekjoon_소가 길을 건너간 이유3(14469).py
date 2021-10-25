n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

prev = 0
for i in arr:
    now = i[0] + i[1]
    if prev < i[0]: # 현재 도착한 소의 시간이 이전 소의 입장시간보다 크다면
        prev =  now # 현재 소의 입장시간을 최종 값으로 정해주기
    elif prev >= i[0]: # 현재 도착한 소의 시간이 이전 소의 입장시간보다 작거나 같다면
        prev += i[1] # 이전 소의 입장 시간에 현재 소의 검문 시간만을 더해주기

print(prev)
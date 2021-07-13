# ex) 공포도 3인 모험가는 3명 이상 모여야 떠날 수 있다.

n = int(input())
x = list(map(int, input().split()))

x.sort(reverse=True)

count = 0
group = 0
while group <= n:
    group += x[group]
    
    if group == n or group > n:
        break

    count += 1

print(count)
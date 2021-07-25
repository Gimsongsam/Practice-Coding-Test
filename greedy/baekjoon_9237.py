n = int(input())
t = list(map(int, input().split()))

t.sort(reverse=True) # 가장 큰 수 부터 정렬

result = [0] * n           # 나무의 갯수 만큼 리스트 만들기
count = 1                  # 나무를 심는 일 수
for i in range(n):         # 나무 갯수 만큼 반복
    result[i] = count            # 나무를 심은 시간으로 리스트 초기화
    result[i] = result[i] + t[i] # 나무가 자라는 시간 더하기
    count += 1             # 나무를 심는 시간 추가

print(max(result) + 1)     # 마지막 나무가 자란 다음 날을 출력
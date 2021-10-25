'''
첫 번째 버튼은 주파수 1MHz 증가시킨다.
두 번째 버튼은 주파수 1MHz 감소시킨다.
나머지 N개의 버튼은 즐겨찾기 기능으로, 미리 지정된 주파수로 이동한다.
'''

A, B = map(int, input().split())  # (1 <= A, B < 1000, a !== B)
n = int(input())
star = [0] * n
for i in range(n):
    star[i] = int(input())

result = [0] * (n + 1)
result[0] = abs(A - B) # 즐겨찾기를 거치지 않은 버튼 클릭 수

i = 1
for j in star: # 가장 가까운 즐겨찾기 주파수 찾기
    result[i]= abs(B - j) + 1  # 버튼 클릭수 1을 추가한 즐겨찾기와 찾아야할 주파수의 버튼 클릭수를 추가
    i += 1

print(min(result))
# 1은 집이 있는 곳, 0은 집이 없는 곳
n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x, y, count):

    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return False
    if arr[x][y] == 1:
        arr[x][y] = count

        dfs(x-1, y, count)
        dfs(x+1, y, count)
        dfs(x, y-1, count)
        dfs(x, y+1, count)
        return True
    return False

count = 2
for i in range(n):
    for j in range(n):
        if True == dfs(i, j, count):
            count += 1

# 총 단지 수 출력하기
print(count - 2)

# 단지내 집의 수를 오름차순으로 출력하기
result_arr = sum(arr,[])
result_arr_count = []
for i in range(2, max(result_arr)+1):
    result_arr_count.append(result_arr.count(i))

result_arr_count.sort()

for i in range(len(result_arr_count)):
    print(result_arr_count[i])
# 5 * 5 숫자판
# 각각의 판에 써져있는 숫자 0 ~ 9
# 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동 -> 총 6자리의 수
# 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 된다.

graph = []
for i in range(5):
    graph.append(list(input().split()))

def dfs(x, y, data):
    # 범위에 좌표값이 들어있는지 확인하기
    if x < 0 or y < 0 or x > 4 or y > 4:
        return False
    
    if len(data) == 6:
        result.add(data)
        return False

    data += graph[x][y]

    dfs(x-1, y, data)
    dfs(x+1, y, data)
    dfs(x, y+1, data)
    dfs(x, y-1, data)
    return True

x = 0
y = 0

data = ""
result = set([])
for i in range(5):
    for j in range(5):
        x, y = i, j
        dfs(x, y, data)

print(len(result))
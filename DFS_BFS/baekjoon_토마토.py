# 며칠이 지나면 토마토들이 모두 익는지 최소 일수를 구하기
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸

# 1과 인접한 노드가 0이라면 1로 바꾸고 익는 일수 더하기
# -1이라면 pass하기
from collections import deque

m, n = map(int, input().split()) # 상자의 크기 m = 가로칸의 수, n = 세로 칸의 수

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# print(data)
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, result):
    queue = deque()
    queue.append(x, y)

    while queue:
        x + dx



    return result


# x, y = 0
result = 0
# bfs(x, y, result)


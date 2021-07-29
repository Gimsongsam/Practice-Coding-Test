from collections import deque

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())

# 그래프 만들기
arr = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

# 노드 배열 모델링하기 -> 작은 번호 부터 정렬
for i in range(len(arr)):
    arr[i].sort()

# DFS 구하기
def dfs(arr, v, visited_dfs):

    visited_dfs[v] = True
    print(v, end=' ')

    for i in arr[v]:
        if not visited_dfs[i]:
            dfs(arr, i, visited_dfs)

visited_dfs = [False] * (n + 1)

dfs(arr, v, visited_dfs)

print()

# BFS 구하기
def bfs(arr, v, visited_bfs):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in arr[pop]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

visited_bfs = [False] * (n + 1)

bfs(arr, v, visited_bfs)
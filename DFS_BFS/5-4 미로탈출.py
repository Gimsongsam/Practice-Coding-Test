from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):

    # n, m 까지(5, 6) 의 최단 거리 구하기 -> 연결된 노드를 모두 돌았을 때 

    # 첫줄의 첫번째 좌표부터 확인하며 한칸씩 이동
    queue = deque([(x, y)])

    while queue:
        visited = queue.popleft()

        # 좌표의 범위가 포함되는지 확인하기 0, 0미만 n, m 초과라면
        if visited[0] < 0 or visited[1] < 0 or visited[0] > n - 1 or visited[1] > m - 1:
            continue
        # 방문한 노드가 만약 1이라면 해당 좌표이동하기
        else:
            if graph[visited[0]][visited[1]] == 1:
                graph[visited[0]][visited[1]] = graph[x][y] + 1
                # graph[visited[0]][visited[1]] = 0
                # result += graph[x][y] + 1
                x = visited[0]
                y = visited[1]

        # 좌 하 우 상 로 연결된 노드들을 탐색하기위해 큐에 상하좌우 노드 큐에 삽입하기
                queue.append((x, y+1))
                queue.append((x+1, y))
                queue.append((x, y-1))
                queue.append((x-1, y))
                
    return graph[n-1][m-1]

x = 0
y = 0

print(bfs(x, y))
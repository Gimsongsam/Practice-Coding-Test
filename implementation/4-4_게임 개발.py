# 내가 푼 코드
n, m = map(int, input().split())

a,b,d = map(int, input().split())
move = [a, b]
# 북, 동, 남, 서 // (수직, 수평)
rotate = [[-1, 0], [0, 1], [1, 0], [0, -1]]
Map = []
for i in range(n):
    Map.append(input().split())

result = 1
count = 0
while True:
    SUM = []
    
    for x,y in zip(move, rotate[d]):
        SUM.append(x+y)

    if Map[move[0]][move[1]] == Map[SUM[0]][SUM[1]]: # 현재위치와 다음 이동 경로의 값이 같다면
        Map[move[0]][move[1]] = -1 # 현재 자리를 이동경로로 표시
        move = [SUM[0], SUM[1]] # 다음 경로로 이동
        result += 1 # 이동횟수 추가
    else: # 회전하기
        SUM = []
        d += 1
        count += 1
        if count >= 3:
            m = rotate[(d + 2) % 4]
            move = [x+y for x,y in zip(move,m)] 
            if int(Map[move[0]][move[1]]) <= 0:
                continue
            else:
                break
            
    if d == 4:
            d = 0    
    
print(result)



# 교재 답안
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction   # 함수 바깥에서 선언된 전역변수이므로 global 키워드를 사용
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = x + dx[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

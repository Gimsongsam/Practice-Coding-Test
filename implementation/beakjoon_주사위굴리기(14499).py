N, M, x, y, k = map(int, input().split())

root = []
for _ in range(N):
     root.append(list(map(int, input().split())))
# print(root)

# 현재 주사위의 좌우면 -> 1, 2
dice_LR = [0, 0]
# 현재 주사위의 상하면 -> 3, 4
dice_UD = [0, 0]
# 현재 주사위의 윗면과 바닥면
dice = [0, 0]

# 상 하 좌 우
command = [(-1, 0), (1, 0), (0, -1), (0, 1)]

move = list(map(int, input().split()))

# print(move)

# 좌표값에 따른 주사위면 복사하고, 출력하기
def simulation(nx, ny, move):

    if move == 1:
        dice_LR[0], dice[1] = dice[1], dice_LR[0]
        dice_LR[1], dice[0] = dice[0], dice_LR[1]
        dice_LR[0], dice_LR[1] = dice_LR[1], dice_LR[0]
    elif move == 2:
        dice_LR[1], dice[0] = dice[0], dice_LR[1]
        dice_LR[0], dice[1] = dice[1], dice_LR[0]
        dice[0], dice[1] = dice[1], dice[0]
    elif move == 3:
        dice_UD[0], dice[1] = dice[1], dice_UD[0]
        dice_UD[1], dice[0] = dice[0], dice_UD[1]
        dice_UD[0], dice_UD[1] = dice_UD[1], dice_UD[0]
    elif move == 4:
        dice_UD[1], dice[0] = dice[0], dice_UD[1]
        dice_UD[0], dice[1] = dice[1], dice_UD[0]
        dice[0], dice[1] = dice[1], dice[0]


    # 이동 후 주사위 윗면 출력하기
    print(dice[0])

    # 이동한 칸에 쓰여 있는 수가 0보다 크다면
    if root[nx][ny] > 0:
        # 칸에 쓰여있는 수를 주사위의 바닥면으로 복사하기
        dice[1] = root[nx][ny]
        # 칸의 수는 0으로 만들기
        root[nx][ny] = 0
        return
    else:
        root[nx][ny] = dice[1]
        return
    

# x, y 좌표값을 복사하기
nx, ny = x, y

# 주사위 굴리기
for i in move:

    # 1이라면 오른쪽으로 이동하기
    if i == 1:
        nx += command[3][0]
        ny += command[3][1]        

    # 2라면 왼쪽으로 이동하기
    elif i == 2:
        nx += command[2][0]
        ny += command[2][1]

    # 3라면 위쪽으로 이동하기
    elif i == 3:
        nx += command[0][0]
        ny += command[0][1]

    # 4라면 아래쪽으로 이동하기
    elif i == 4:
        nx += command[1][0]
        ny += command[1][1]
    
    print('좌표값: ', nx, ny)
    if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
        # 범위를 벗어난다면 초기화하기
        nx, ny = x, y
        continue
    
    # 범위에 들어간다면 x, y 좌표값 설정
    x, y = nx, ny
    
    # print('현재 좌표: ', x, y)
    # print('주사위 상하: ', dice_UD)
    # print('주사위 좌우: ', dice_LR)
    # print('주사위 위아래', dice)

    simulation(nx, ny, i)

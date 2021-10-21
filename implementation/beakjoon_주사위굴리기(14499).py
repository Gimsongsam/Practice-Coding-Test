# 첫째 줄에 지도의 세로 크기 N,
# 가로 크기 M (1 ≤ N, M ≤ 20), 
# 주사위를 놓은 곳의 좌표 x y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1),
# 명령의 개수 K (1 ≤ K ≤ 1,000)

# 둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로,
# 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다.
# 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

# 이동한 칸에 쓰여 있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

# 이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다.
# 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

N, M, x, y, k = map(int, input().split())

# map = [[] for _ in range(N)]

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
def simulation(x, y, move):

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
    if root[x][y] > 0:
        # 칸에 쓰여있는 수를 주사위의 바닥면으로 복사하기
        dice[1] = root[x][y]
        # 칸의 수는 0으로 만들기
        root[x][y] = 0
        return
    else:
        root[x][y] = dice[1]
        return
    


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
    
    if x < 0 or y < 0 or x > N-1 or y > M-1:
        # 범위를 벗어난다면 초기화하기
        nx, ny = x, y
        continue

    x, y = nx, ny
    print('현재 좌표: ', x, y)
    # print('주사위 상하: ', dice_UD)
    # print('주사위 좌우: ', dice_LR)
    # print('주사위 위아래', dice)

    simulation(x, y, i)

from collections import deque

def solution(numbers, hand):
    left = [1, 4, 7]
    right = [3, 6, 9]
    middled = [2, 5, 8, 0]

    # keypad = [[0] * 3 for _ in range(3)]
    # number = 1
    # for i in range(3):
    #     for j in range(3):
    #         keypad[i][j] = number
    #         number += 1
    # keypad.append(['*', 0, '#'])
    
    L_hand = (3, 0)
    R_hand = (3, 2)

    # 상 하 좌 우로 탐색하기, (x, y)
    # move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # queue = deque([])

    for i in numbers:
        # 해당 숫자가 1, 4, 7 중 하나라면
        if i in left:
            print('L')
            L_hand = (left.index(), 0)
        # 해당 숫자가 3, 6, 9 중 하나라면
        elif i in right:  
            print('R')
            R_hand = (right.index(), 2)
        # 해당 숫자가 2, 5, 8, 0 중 하나라면 
        # else:
            # 왼손과 오른손의 거리를 비교하기
            # queue.append(L_hand)
            # serch = queue.popleft()

            # 현재 손가락의 위치가 키패드보다 크다면 -1 하기
            # 현재 손가락의 위치가 키패드 보다 크다면 +1 하기
            # 


    # answer = ''
    # return answer

    # print(keypad)

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")


# print((left.index(1),0))

# test = [1, 2, 3, 4, 5]
# print(1 in test)
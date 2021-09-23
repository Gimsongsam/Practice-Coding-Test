def solution(board, moves):
    
    stack = []
    answer = 0

    for i in moves:    
        # 위치에 해당하는 인형을 뽑기
        
        # 현재 탐색하는 위치가 빈칸인지 아닌지 탐색
        line = 0
        
        while True:
            # 마지막 라인이상이라면 탈출하기
            if line > len(board)-1:
                break
            # 빈칸이라면 아랫줄에 인형이있는지 탐색
            if board[line][i-1] == 0:
                line += 1
            # 인형이 있다면 바구니에서 인형을 뽑기
            else:
                stack.append(board[line][i-1])
                board[line][i-1] = 0
                break  
        # print(stack)
        
        while len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2 # 인형의 갯수 추가하기
            else:
                break
        
    return answer

print(solution([
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ], [1,5,3,5,1,2,1,4]))
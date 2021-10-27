def solution(dartResult):
    
    score = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    # dartResult 쪼개기
    data = []
    tem = False
    index = 0
    for i in dartResult:
        
        if i in score:
            if tem == True:
                data[index-1] = data[index-1] + i
            else:
                data.append(i)
                tem = True
                index += 1
        else:
            data.append(i)
            index += 1
            tem = False

    answer = []
    score_index = -1
    # 구현
    for i in data:
    
        print(i)
        if i in score:
            answer.append(int(i))
            score_index += 1
        elif i in bonus:
            answer[score_index] = answer[score_index] ** bonus[i]
        elif i == '*':
            # 현재 인덱스가 0 초과라면
            if score_index > 0:
                # 이전 인덱스 점수에도 효과주기
                answer[score_index-1] = answer[score_index-1] * 2
            answer[score_index] = answer[score_index] * 2
        elif i == '#':
            answer[score_index] = -answer[score_index]

    return sum(answer)

print(solution('1D2S#10S'))
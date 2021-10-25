def solution(lottos, win_nums):
    
    # 0은 당첨 가능한 최고 순위 1은 최저 순위
    result = [0] * 2
    for i in range(6):
        if lottos[i] == 0:
            result[0] += 1
            continue
        for j in range(6):
            if lottos[i] == win_nums[j]:
                result[0] += 1
                result[1] += 1
    
    answer = [0] * 2
    rank = [6, 5, 4, 3, 2, 1, 6]
    answer[0] = rank[result[0]-1]
    answer[1] = rank[result[1]-1]
    
    return answer
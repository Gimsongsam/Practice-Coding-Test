def solution(nums):

    poketmon = len(set(nums)) # 중복되지 않는 포켓몬의 수
    num = len(nums) / 2 # N / 2

    if poketmon > num:
        answer = num
    elif poketmon < num:
        answer = poketmon
    else:
        answer = poketmon
    
    return answer

print(solution([3,3,3,2,2,4]))

# Best Code
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
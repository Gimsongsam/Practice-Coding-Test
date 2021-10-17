# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 

def solution(N, stages):
    answer = []
    user = len(stages)

    for i in range(5):
        failure = stages.count(i+1) / (user)

        # stages.count(i+1) - 
        
        print(stages.count(i+1), '/', (stages.count(i+1) - user), '=', failure)

    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])


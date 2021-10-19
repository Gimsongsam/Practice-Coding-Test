# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 

def solution(N, stages):
    
    user = len(stages)

    data = {}
    for i in range(N):
        # print('탐색하고있는 스테이지:', i+1)

        # 실패율 계산
        if user == 0: # 0으로 나눌 수 없기 때문에 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의
            failure = 0
        else:
            failure = stages.count(i+1) / (user)
        # print(stages.count(i+1), '/', user, '=', failure)
        data[i+1] = failure
        print(data)

        # 다음 스테이지 실패율 계산을 위해 실패한 참가자 수 만큼 user 수를 빼기
        user -= stages.count(i+1)
        # print('남은 유저 수: ', user)

    answer = sorted(data.items(), reverse=True, key=lambda item: item[1])
    # print('최종 데이터: ', answer)

    return [i[0] for i in answer]

print(solution(5, [2, 2, 2, 2, 2]))


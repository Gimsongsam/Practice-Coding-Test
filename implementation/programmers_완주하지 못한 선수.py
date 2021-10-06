def solution(participant, completion):

    # 참가자 명단을 딕셔너리 자료형으로 만들기
    participant_table = {}
    for i in range(len(participant)):
        if participant[i] in participant_table:
            participant_table[participant[i]] += 1
        else: 
            participant_table[participant[i]] = 1
    
    # 순차적으로 완주자의 명단을 순회하며 딕셔너리 자료형에 키값이 있는지 조회
    for i in completion:
        if i in participant_table:
            participant_table[i] -= 1
            if participant_table[i] == 0:
                del participant_table[i]
        # 없다면 continue
        else:
            continue

    answer = list(participant_table.keys())
    return answer[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# best CODE
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    print(collections.Counter(participant))
    print(collections.Counter(completion))

    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
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



# def solution(participant, completion):
#     completion.sort()
#     target_arr = participant.copy()

#     def binary_search(completion, target, start, end):
#         if start > end:
#             return None
#         mid = (start + end) // 2
#         # 찾은 경우 중간점 인덱스 반환
#         if completion[mid] == target:
#             target_arr.remove(completion[mid])
#             completion.remove(completion[mid])
#             return
#         # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#         elif completion[mid] > target:
#             return binary_search(completion, target, start, mid - 1)
#         # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#         else: 
#             return binary_search(completion, target, mid + 1, end)

#     for i in range(len(participant)):
#             start = 0
#             end = len(completion) - 1
#             binary_search(completion, participant[i], start, end)

#     # print(completion)
#     # print(target_arr)
    
#     return target_arr[0]

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

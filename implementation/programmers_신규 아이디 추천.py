from collections import deque

def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id.lower()

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    token = '~!@#$%^&*()=+[{]}:?,<>/'
    for remove in token:
        new_id = new_id.replace(remove, "")
        # print(remove)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    # 첫 번째 인덱스는 이전 값이 없으므로 이전값과 비교할 수 없으므로 .이 아니라면 추가해주기
    id_arr = deque([])
    # if new_id[0] != ".":
    id_arr.append(new_id[0])
    # 각 인덱스로 접근하여 이전 문자열이 .인지 아닌지 조건을 검사
    for i in range(1, len(new_id)):    
        # 현재 인덱스의 값이 일반문자열이고 이전의 인덱스 값이 .이라면 .과 현재 인덱스 값을 추가하기
        if new_id[i] != ".":
            if new_id[i-1] == '.':
                id_arr.append(".")
                id_arr.append(new_id[i])
            # 현재 인덱스의 값이 일반문자열이라면 추가해주기
            else:
                id_arr.append(new_id[i])
        # .이라면 continue
        else:
            continue

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if id_arr[0] == '.' or id_arr[-1] == '.':

        for i in range(len(id_arr)):
            if len(id_arr) > 0:
                if id_arr[0] == '.':
                    id_arr.popleft()
            if len(id_arr) > 0:
                if id_arr[-1] == '.':
                    id_arr.pop()

    new_id = (''.join(id_arr))

    
    
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[-1:]
    
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        for _ in range(3):
            # 3이 될 때 까지만 반복하기 위한 조건
            if len(new_id) <= 2:
                new_id = new_id + new_id[-1]
            else:
                break
    
    answer = new_id
    return answer

print(solution("abcdefghijklmn.p"))
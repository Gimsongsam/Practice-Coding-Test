case = ['Enter', 'Leave', 'Change']

def change(info, user):

    # Change
    if case[2] == info[0]:
        user[info[1]] = info[2]
    # Enter
    elif case[0] == info[0]:
        user[info[1]] = info[2]
    # Leave
    else:
        return

def solution(record):
    answer = []
    
    user = {}
    info = []
    for i, j in enumerate(record):
        info.append(j.split())
        change(info[i], user)
    
    for i in info:
        # Change
        if case[2] == i[0]:
            continue
        # Enter
        elif case[0] == i[0]:
            answer.append('{0}님이 들어왔습니다.'.format(user[i[1]]))
        # Leave
        else:
            answer.append('{0}님이 나갔습니다.'.format(user[i[1]]))
    
    return answer
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])



# Best Code
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
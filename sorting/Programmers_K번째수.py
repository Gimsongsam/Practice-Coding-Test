def solution(array, commands):

    answer = []
    
    for i in range(len(commands)):
        if commands[i][0] == commands[i][1]:
            slicing = [array[commands[i][0] - 1]]
        else:
            # if commands[i][1] == len(array):
            #     slicing = array[commands[i][0] - 1 :]
            # else:
            slicing = array[commands[i][0] - 1 : commands[i][1]]
            slicing.sort()

        answer.append(slicing[commands[i][2] - 1])
        print(slicing)
    
    # print(answer)
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# best solution
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
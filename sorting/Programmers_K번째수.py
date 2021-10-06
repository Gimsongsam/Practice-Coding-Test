def solution(array, commands):

    answer = []

    for i in range(len(commands)):
        if commands[i][0] == commands[i][1]:
            slicing = [array[commands[i][0] - 1]]
        else:
            if commands[i][1] == len(array):
                slicing = array[commands[i][0] - 1 : - 1]
            else:
                slicing = array[commands[i][0] - 1 : commands[i][1]]
            slicing.sort()

            # print(commands[i][0] - 1, ',', commands[i][1] - 1)
            # print('slicing: ', slicing)
        
        answer.append(slicing[commands[i][2] - 1])
    
    # print(answer)
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
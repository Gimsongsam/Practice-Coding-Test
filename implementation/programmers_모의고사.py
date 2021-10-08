
def solution(answers):
    x = [1, 2, 3, 4, 5]
    y = [2, 1, 2, 3, 2, 4, 2, 5]
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    def search(answers, student):
        count = 0
        index = 0
        for i in range(len(answers)):
            # 현재 비교하는 수포자의 리스트가 마지막 인덱스라면
            if len(student)-1 == index:
                index = 0 # 처음부터 비교
            if answers[i] == student[index]:
                count += 1
            index += 1

        return count
        
    result = []
    for i in x, y, z:
        result.append(search(answers, i))
    
    # print(result)
    winner = max(result)
    answer = [i + 1 for i in range(len(result)) if result[i]==winner]

    return answer 

print(solution([1,2,3,4,5]))
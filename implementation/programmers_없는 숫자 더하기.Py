def solution(numbers):
    search = []
    for i in range(10):
        if numbers.count(i) <= 0:
            search.append(i)

    return sum(search)

solution([1,2,3,4,6,7,8,0])
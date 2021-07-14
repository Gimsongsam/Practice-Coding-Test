def solution(food_times, k):
    count = 0
    num = 0
    while count <= k:
        if food_times[num] > 0:
            food_times[num] = food_times[num] - 1
            count += 1
        else:
            continue
        num += 1
        if num >= len(food_times):
            num = 0

    answer = num
    return answer


print(solution([3, 1, 2], 5))
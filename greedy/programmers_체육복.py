# n (전체 학생의 수)
# lose (체육복을 도난당한 학생들의 번호)
# reserve (여벌의 체육복을 가져온 학생들의 번호)
# 체육수업을 들을 수 있는 학생의 최댓값 return

# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다.
# !여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

def solution(n, lost, reserve):
    lost.sort()

    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 경우의 reseve 배열
    reserve_data = reserve.copy()
    for i in reserve:
        if i in lost:
            reserve_data.remove(i)
            lost.remove(i)

    for i in lost:
        if i-1 in reserve_data:
            reserve_data.remove(i-1)
        elif i+1 in reserve_data:
            reserve_data.remove(i+1)
        else:
            n -= 1

    return n

print(solution(10, [5, 4, 3, 2, 1], [3, 1, 2, 5, 4]))

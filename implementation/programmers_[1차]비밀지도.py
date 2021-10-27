from collections import deque
def solution(n, arr1, arr2):

    def binary(arr):
        n_arr = [0] * n

        for i in range(n):
            binary = deque(list(format(arr[i], 'b')))

            if len(binary) < n:
                for _ in range((n - len(binary))):
                    binary.appendleft('0')

            n_arr[i] = list(binary)

        return n_arr

    n_arr1 = binary(arr1)
    n_arr2 = binary(arr2)

    answer = [''] * n

    for i, (arr1, arr2) in enumerate(zip(n_arr1, n_arr2)):
        
        for j in range(n):
            if arr1[j] == '0' and arr2[j] == '0':
                answer[i] = answer[i] + ' '
            elif arr1[j] == '1' or arr2[j] == '1':
                answer[i] = answer[i] + '#'
    return answer


# Best Code
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
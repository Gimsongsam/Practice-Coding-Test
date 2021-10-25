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

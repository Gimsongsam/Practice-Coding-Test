from itertools import combinations
import math

def solution(nums):

    count = 0
    # 리스트가 조합될 수 있는 경우의 수 구해주기
    for i in combinations(nums, 3):
        # 조합을 더하여 소수인지 아닌지 판별해주기
        # 조합되어 더해진 수의 제곱근까지의 모든 수를 확인하며
        com = sum(i)

        for j in range(2, int(math.sqrt(com))+1):

            # 조합된 수가 해당 수로 나누어떨어진다면
            if com % j == 0:
                temp = False
                break # 소수가 아님
            else:
                temp = True

        # 모든 제곱근의 수가 나누어 떨어지지 않는다면 count 추가하기
        if temp == True:
            count += 1
        
    return count

print(solution([1,2,7,6,4]))
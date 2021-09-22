
def solution(numbers, hand):
    answer = ''

    left = [1, 4, 7]
    right = [3, 6, 9]
    middled = [2, 5, 8, 11]
    
    L_hand = 10
    R_hand = 12

    for i in numbers:
        # 거리 비교를 위해 0은 11롤 만들어버리기
        if i == 0:
            i = 11
        # 해당 숫자가 1, 4, 7 중 하나라면
        if i in left:
            answer = answer + 'L'
            L_hand = i
        # 해당 숫자가 3, 6, 9 중 하나라면
        elif i in right:  
            answer = answer + 'R'
            R_hand = i
        # 해당 숫자가 2, 5, 8, 0 중 하나라면 
        else:
            # 왼손과 오른손의 거리를 비교하기
            L_count = 0
            R_count = 0
            L = L_hand
            R = R_hand

            while L != i:    
                # 타켓숫자와 거리 구하기
                # 타켓숫자와의 거리가 2이상이라면
                if L - i >= 2:
                    L -= 3
                    L_count += 1
                # 타켓숫자와의 거리가 -2이하이라면
                elif L - i <= -2:
                    L += 3
                    L_count += 1
                # 타겟숫자와의 거리가 -1이라면
                elif L - i == -1:
                    L += 1
                    L_count += 1
            
            while R != i:
                # 타켓숫자와 거리 구하기
                # 타켓숫자와의 거리가 2이상이라면
                if R - i >= 2:
                    R -= 3
                    R_count += 1
                # 타켓숫자와의 거리가 -2이하이라면
                elif R - i <= -2:
                    R += 3
                    R_count += 1
                # 타겟숫자와의 거리가 1이라면
                elif R - i == 1:
                    R -= 1
                    R_count += 1
            
            if L_count > R_count:
                answer = answer + 'R'
                R_hand = i
            elif L_count < R_count:
                answer = answer + 'L'
                L_hand = i
            elif L_count == R_count:
                if hand == 'right':
                    answer = answer + 'R'
                    R_hand = i
                else:
                    answer = answer + 'L'
                    L_hand = i
    
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))


# print((left.index(1),0))

# test = [1, 2, 3, 4, 5]
# print(1 in test)
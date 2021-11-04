from itertools import combinations

# course 수에 따른 손님들의 조합구하기
def combination(order, course):
    data = {}
    
    for i in order:
        i = list(i)
        i.sort()
        combi = list(combinations(i,course))

        for x in combi:
            food = "".join(x)
            if food in data:
                data[food] += 1
            else:
                data[food] = 1
    
    return data

def solution(orders, course):
    
    answer = []
    
    for i in course:
        combi = combination(orders, i)
        
        if len(combi) < 1:
            continue
        else:
            result = [k for k,v in combi.items() if max(combi.values()) == v and 1 < v]
            for i in result:
                answer.append(i)
    
    answer.sort()
        
    return answer
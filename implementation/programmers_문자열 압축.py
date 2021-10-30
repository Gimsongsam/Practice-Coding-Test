def solution(s):
    
    len_s = len(s)
    
    def implementation(index):
    
        # 문자열을 단위별로 자르기
        pattern = []
        
        start = 0
        last = index

        while last < len_s:
            pattern.append(s[start:last])
            start += index
            last += index
        
        pattern.append(s[index * int(len_s / index):])
            
        # 가장 짧은 문자열로 구현하기
        result = ''
        tem = {pattern[0] : 1}
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[i-1]:
                tem[pattern[i]] += 1
            else:
                item = list(tem.items())
                # print('item: ', item)
                
                if item[0][1] == 1:
                    result += item[0][0]
                else:
                    result += str(item[0][1]) + item[0][0]
                tem = {}
                tem[pattern[i]] = 1
                
        item = list(tem.items())
        
        if item[0][1] == 1:
            result += item[0][0]
        else:
            result += str(item[0][1]) + item[0][0]
        
        # print('최종: ', result)
        return result
    
    if len_s > 1:
        parse = [i for i in range(1, len_s)]
    else:
        return len_s

    for i in range(len(parse)):
        parse[i] = implementation(parse[i])
    
    
    answer = min(parse, key = lambda s: len(s))
    # print(answer)
    return len(answer)

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("x"))
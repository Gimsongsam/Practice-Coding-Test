def solution(s):
    
    len_s = len(s)
    
    # 문자열을 단위별로 자르기
    def implementation(index):
        
        pattern = []
        
        start = 0
        last = index
        while last <= len_s:
            pattern.append(s[start:last])
            start += index
            last += index
        
        # print(pattern)
            
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
                # print('result: ', result)
                tem = {}
                tem[pattern[i]] = 1
                
        item = list(tem.items())
        
        if item[0][1] == 1:
            result += item[0][0]
        else:
            result += str(item[0][1]) + item[0][0]
        
        # print('최종: ', result)
        
        return result
    
    
    parse = [i for i in range(1, len_s) if len_s % i == 0]
    # parse = [i for i in range(1, len_s)]
    # print(parse)
    
    for i in range(len(parse)):
        # print('parse: ', parse[i])
        parse[i] = implementation(parse[i])
    
    # print(parse)
    
    
    answer = min(parse)
    # print(answer)
    return len(answer)
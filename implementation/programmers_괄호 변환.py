def simulation(array, start):
    
    for i in range(start, len(array)):
        if array[i] == '(':
            array[i] = ')'
        else:
            array[i] = '('
        
        tem = 0
        for x in array:
            if x == '(':
                tem += 1
            else:
                tem -= 1

            if tem < 0 :
                simulation(array, start + 1)
        
    return array
    

def solution(p):
    
    parse_p = list(p)
    
    while True:
        
        tem = 0
        for i, j in enumerate(parse_p):
            if j == '(':
                tem += 1
            else:
                tem -= 1

            if tem < 0:
                if parse_p[i] == '(':
                    parse_p[i] = ')'
                else:
                    parse_p[i] = '('

                break
        
        if tem == 0:
            break
        else:
            parse_p = simulation(parse_p, 0)
        
        print(parse_p)
    
    return "".join(parse_p)


solution("()))((()"	)
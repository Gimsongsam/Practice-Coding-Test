def solution(s):
    token_arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for find in token_arr:
        if find in s:
            s = s.replace(find, str(token_arr.index(find))) 

    answer = int(s)
    return answer
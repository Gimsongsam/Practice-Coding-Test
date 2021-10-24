def solution(a, b):
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    now_week = 5
    
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    date = 0
    
    def week_calc(date, now_week):
        # 무슨 요일인지 계산
        nextWeek = date % 7
        now_week = (now_week - 1 + nextWeek) % 7
        return now_week
    
    for i in range(a - 1):
        # 개월 수 만큼 일 수 추가
        date += month[i]
        week_calc(date, now_week)
    # 일 수 추가
    date += b
    
    return week[week_calc(date, now_week)]
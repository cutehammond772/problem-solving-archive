def solution(routes):
    answer = 0
    start, end = -30001, -30001
    
    # 라인 스위핑
    routes.sort()
    
    for x, y in routes:
        if end < x:
            start, end = x, y
            answer += 1
            continue
        
        start, end = max(start, x), min(end, y)
    
    return answer
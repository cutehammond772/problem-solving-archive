def solution(routes):
    answer = 0
    end = -30001
    
    # 라인 스위핑
    routes.sort()
    
    for x, y in routes:
        if end < x:
            end = y
            answer += 1
            continue
        
        end = min(end, y)
    
    return answer
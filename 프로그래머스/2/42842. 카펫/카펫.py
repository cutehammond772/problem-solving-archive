def solution(brown, yellow):
    answer = [0, 0]
    
    for h in range(1, int(yellow ** 0.5) + 1):
        if yellow % h:
            continue
        
        w = yellow // h
        
        if (w + h + 2) * 2 == brown:
            answer = [w + 2, h + 2]
    
    return answer
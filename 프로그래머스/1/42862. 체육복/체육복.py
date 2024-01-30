def solution(n, lost, reserve):
    answer = 0
    status = [1] * (n + 2)
    
    # 1 ~ n번째 학생만 고려함.
    status[0] = status[n + 1] = 0
    
    for lost_student in lost:
        status[lost_student] -= 1
    
    for reserve_student in reserve:
        status[reserve_student] += 1
    
    for student in range(1, n + 1):
        answer += 1
        
        if status[student] != 0:
            continue
        
        # 왼쪽 학생부터 먼저 판단한다.
        if status[student - 1] > 1:
            status[student - 1] -= 1
            status[student] = 1
        
        elif status[student + 1] > 1:
            status[student + 1] -= 1
            status[student] = 1
        
        # 체육복을 빌릴 수 없는 경우를 나타낸다.
        else:
            answer -= 1
    
    return answer
    
def solution(n, lost, reserve):
    answer = n
    
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    
    for student in _lost:
        if student - 1 in _reserve:
            _reserve.remove(student - 1)
        
        elif student + 1 in _reserve:
            _reserve.remove(student + 1)
        
        else:
            answer -= 1
        
    return answer
    
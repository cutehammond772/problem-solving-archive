def solution(s):
    left, right = 0, 0
    valid = True
    
    for bracket in s:
        left += bracket == '('
        right += bracket == ')'
        
        valid = valid and (left - right >= 0)
    
    valid = valid and left == right
    return valid
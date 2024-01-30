def check(end, rocks, n, min_limit):
    distance = end
    offset = 0
    
    for i in range(len(rocks)):
        if (rocks[i] - offset < min_limit) and (n > 0):
            n -= 1
            continue
        
        distance = min(distance, rocks[i] - offset)
        offset = rocks[i]
    
    if n == 0:
        distance = min(distance, end - offset)
    
    return distance >= min_limit

def solution(distance, rocks, n):
    x, y = 0, distance + 1
    
    rocks = [*sorted(rocks)]
    
    while x < y:
        mid = (x + y) // 2
        
        if check(distance, rocks, n, mid):
            x = mid + 1
        else:
            y = mid
    
    return x - 1
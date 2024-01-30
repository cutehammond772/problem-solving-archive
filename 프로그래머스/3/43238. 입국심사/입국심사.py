def check(n, times, limit):
    for time in times:
        n -= min(n, limit // time)
    
    return n == 0

# Parametric Search
def solution(n, times):
    x, y = 1, int(1e18)
    
    while x < y:
        mid = (x + y) // 2
        
        if check(n, times, mid):
            y = mid
        else:
            x = mid + 1
    
    return x
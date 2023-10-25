import sys

sys.setrecursionlimit(10 ** 6)
INF = 1000001

def solution(x, y, n):
    memo = [INF] * 1000001
    memo[x] = 0
    
    for i in range(x, y):
        if i * 2 <= y:
            memo[i * 2] = min(memo[i * 2], memo[i] + 1)
            
        if i * 3 <= y:
            memo[i * 3] = min(memo[i * 3], memo[i] + 1)
                              
        if i + n <= y:
            memo[i + n] = min(memo[i + n], memo[i] + 1)
    
    return memo[y] if memo[y] < INF else -1
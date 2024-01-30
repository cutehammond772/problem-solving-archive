MOD = int(1e9 + 7)

def solution(m, n, puddles):
    memo = [[0] * m for _ in range(n)]
    memo[0][0] = 1
    
    puddle = [[False] * m for _ in range(n)]
    
    for col, row in puddles:
        puddle[row - 1][col - 1] = True
    
    for row in range(n):
        for col in range(m):
            if puddle[row][col]:
                continue
            
            if row > 0:
                memo[row][col] += memo[row - 1][col]
            
            if col > 0:
                memo[row][col] += memo[row][col - 1]
            
            memo[row][col] %= MOD
    
    return memo[n - 1][m - 1]
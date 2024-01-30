def solution(triangle):
    memo = [[0] * x for x in range(1, len(triangle) + 1)]
    
    # 맨 꼭대기
    memo[0][0] = triangle[0][0]
    
    for depth in range(1, len(triangle)):
        memo[depth][0] = triangle[depth][0] + memo[depth - 1][0]
        memo[depth][depth] = triangle[depth][depth] + memo[depth - 1][depth - 1]
        
        for x in range(1, depth):
            memo[depth][x] = triangle[depth][x] + max(memo[depth - 1][x - 1], memo[depth - 1][x])
        
    return max(memo[len(triangle) - 1])
def solution(sequence):
    N = len(sequence)
    dp = [[0] * 2 for _ in range(N)]
    result = -100001
    
    # 0번째
    dp[0][0], dp[0][1] = sequence[0], -sequence[0]
    result = max(result, dp[0][0], dp[0][1])
    
    for x in range(1, N):
        dp[x][0] = max(dp[x - 1][1] + sequence[x], sequence[x])
        dp[x][1] = max(dp[x - 1][0] - sequence[x], -sequence[x])
        result = max(result, dp[x][0], dp[x][1])

    return result
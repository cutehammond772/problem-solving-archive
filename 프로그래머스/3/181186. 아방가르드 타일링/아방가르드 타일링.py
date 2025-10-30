def solution(n):
    # 각 블럭의 조합으로, 직사각형이 될 수 있는 조합에 대해 생각해보아야 한다.
    dp = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    
    MOD = 1e9 + 7
    
    # 초기 값 설정
    init = [1, 1, 3, 10]
    init2 = [1, 1, 3, 11]
    
    for x in range(min(4, n + 1)):
        dp[x] = init[x]
        dp2[x] = init2[x]
    
    for x in range(4, n + 1):
        # case 1. 1x3
        # x
        # x
        # x
        dp[x] = (dp[x] + dp[x - 1]) % MOD
        
        # case 2. (2+3k) x 3
        # aaxxx
        # axxxb
        # xxxbb
        dp[x] = (dp[x] + dp2[x - 2] * 2) % MOD
        # dp[x - 2] + dp[x - 5] + dp[x - 8] + ...
        
        # case 3. (3+3k) x 3
        # aatttb xxx
        # atttbb xxx
        # tttxxx xxx
        dp[x] = (dp[x] + dp[x - 3] + dp2[x - 3] * 4) % MOD
        
        # case 4. (4+3k) x 3
        # otttxxx
        # ootttcc
        # xxxtttc
        dp[x] = (dp[x] + dp2[x - 4] * 2) % MOD
        
        # 누적 값
        dp2[x] = (dp[x] + dp2[x - 3]) % MOD
        
    return dp[n]
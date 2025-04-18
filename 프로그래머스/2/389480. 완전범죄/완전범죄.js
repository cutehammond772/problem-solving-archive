function solution(info, n, m) {
    // 특정 물건은 A 또는 B가 무조건 훔치게 된다.
    // 모든 물건을 훔쳤을 때, "붙잡히지 않는 조건" 하에서 "A의 누적 흔적이 최소"여야 한다.
    // 1. 각 물건을 훔칠 때마다, 가능한 비용에 체크한다.
    // -> 0 <= a, b <= 120에 대해, dp[a + x][b] = dp[a][b + y] = i
    // 2. 위의 식에서, 해당 배열 내 값이 i여야만 체크되도록 한다.
    const dp = [...Array(n)].map(() => Array(m).fill(-1));
    dp[0][0] = 0;
    
    for (let i = 0; i < info.length; i++) {
        const [aCost, bCost] = info[i];
        
        for (let a = n - 1; a >= 0; a--) {
            for (let b = m - 1; b >= 0; b--) {
                if (dp[a][b] !== i) continue;
                
                if (a + aCost < n)
                    dp[a + aCost][b] = i + 1;
                
                if (b + bCost < m)
                    dp[a][b + bCost] = i + 1;
            }
        }
    }
    
    let answer = 120;
    
    for (let a = 0; a <= n - 1; a++) {
        for (let b = 0; b <= m - 1; b++) {
            if (dp[a][b] !== info.length) continue;
            
            answer = Math.min(answer, a);
        }
    }
    
    return answer === 120 ? -1 : answer;
}
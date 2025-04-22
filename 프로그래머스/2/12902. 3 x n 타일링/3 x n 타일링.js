function solution(n) {
    const MOD = 1e9 + 7;
    const dp = Array(5001).fill(0);
    let acc = 0;
    
    // 초기값 설정
    dp[0] = 1;
    dp[1] = 0;
    dp[2] = 3;
    dp[3] = 0;
    
    // 가로의 길이가 홀수이면 배치하는 방법이 없다.
    for (let i = 4; i <= 5000; i += 2) {
        // 가로 2칸을 차지할 경우에는 3가지 경우의 수가 존재한다.
        dp[i] = (dp[i] + (dp[i - 2] * 3) % MOD) % MOD;
        dp[i] = (dp[i] + 2 * (acc += dp[i - 4])) % MOD;
    }
    
    return dp[n];
}
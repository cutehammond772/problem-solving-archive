function solution(n) {
    if (n === 0)
        return 0;
    
    // 약수 특성상 양끝이 대칭을 이루므로 1 ... sqrt(n)까지만 판단해도 됨
    const candidate = [
        ...Array(Math.floor(Math.sqrt(n))).keys()
    ].map((x) => x + 1)
    
    const answer = candidate.reduce((sum, num) => {
        // num이 약수가 아닌 경우
        if (n % num !== 0) return sum;
        
        // num, n / num -> 대칭
        const [a, b] = [num, n / num];
        
        // 서로 같으면 하나만 취급
        if (a === b) return sum + a;
        
        return sum + a + b;
    }, 0);
    
    return answer;
}
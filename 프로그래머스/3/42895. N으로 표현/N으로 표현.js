function solution(N, number) {
    // N을 1개부터 8개까지 나열했을 때 각각 분할 정복으로 접근해야 한다.
    const numbers = Array(9).fill(null);
    const consecutive = [0, 1, 11, 111, 1111, 11111, 111111, 1111111, 11111111];
    
    function resolve(K) {
        if (numbers[K]) {
            return numbers[K];
        }
        
        if (K === 1) {
            (numbers[K] = new Set()).add(N);
            return numbers[K];
        }
        
        // Set 초기화
        numbers[K] = new Set();
        numbers[K].add(consecutive[K] * N);
        
        for (let i = 1; i <= Math.floor(K / 2); i++) {
            const [left, right] = [resolve(i), resolve(K - i)];
            
            for (const x of left) {
                for (const y of right) {
                    // ADD
                    numbers[K].add(x + y);
                    
                    // SUBTRACT
                    numbers[K].add(x - y);
                    numbers[K].add(y - x);
                    
                    // MULTIPLY
                    numbers[K].add(x * y);
                    
                    // DIVIDE
                    numbers[K].add(Math.floor(x / y));
                    numbers[K].add(Math.floor(y / x));
                } 
            }
        }
        
        return numbers[K];
    }
    
    for (let i = 1; i <= 8; i++) {
        if (resolve(i).has(number)) {
            return i;
        }
    }
    
    return -1;
}
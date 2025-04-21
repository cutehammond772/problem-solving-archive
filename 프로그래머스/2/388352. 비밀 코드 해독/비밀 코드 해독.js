function solution(n, q, ans) {
    const combinations = [];
    
    // 서로 다른 숫자 뽑아내기 : nC5
    for (let a = 1; a <= n - 4; a++) {
        for (let b = a + 1; b <= n - 3; b++) {
            for (let c = b + 1; c <= n - 2; c++) {
                for (let d = c + 1; d <= n - 1; d++) {
                    for (let e = d + 1; e <= n; e++) {
                        const node = Array(n + 1).fill(false);
                        
                        node[a] = node[b] = node[c] = node[d] = node[e] = true;
                        combinations.push(node);
                    }
                }
            }
        }
    }
    
    const answer = combinations.filter((node) => {
        for (let i = 0; i < q.length; i++) {
            let count = 0;
            
            for (const num of q[i]) {
                if (node[num]) {
                    count++;
                }
            }
            
            if (ans[i] !== count) {
                return false;
            }
        }
        
        return true;
    }).length;
    
    return answer;
}
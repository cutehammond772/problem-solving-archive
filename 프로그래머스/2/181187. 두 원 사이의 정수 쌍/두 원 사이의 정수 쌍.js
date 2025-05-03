function solution(r1, r2) {
    let answer = 0;
    // 원과 x축과 평행한 선 (y = n)의 교점을 각각 구한 다음, floor 처리하면 된다.
    
    function dots(r) {
        let result = 0;
        let onCircle = 0;
        
        // (y = -n) ~ (y = n)
        for (let n = -r; n <= r; n++) {
            x = Math.sqrt(r ** 2 - n ** 2)
            
            if (x === 0) {
                onCircle += 1;
            }
            else if (Math.floor(x) === x) {
                onCircle += 2;
            }
            
            result += 2 * Math.floor(x) + 1;
        }
        
        return { result, onCircle };
    }
    
    const dotsOfR1 = dots(r1);
    const dotsOfR2 = dots(r2);
    
    return dotsOfR2.result - dotsOfR1.result + dotsOfR1.onCircle;
}
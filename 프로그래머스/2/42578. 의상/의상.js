function solution(clothes) {
    const groups = new Map();
    
    // 1. 의상 등록
    for (const [name, type] of clothes) {
        if (!groups.has(type)) {
            groups.set(type, []);
        }
        
        groups.set(type, [...groups.get(type), name]);
    }
    
    // 2. 조합 계산하기
    let combinations = 1;
    
    for (const [type, entries] of groups) {
        combinations *= (entries.length + 1);
    }
    
    // 3. 정답
    const answer = combinations - 1;
    
    return answer;
}
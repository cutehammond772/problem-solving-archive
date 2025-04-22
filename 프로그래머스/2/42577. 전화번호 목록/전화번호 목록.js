function solution(phone_book) {
    // 각 문자열의 모든 접두사를 등록
    const count = new Map();
    
    for (const phoneNum of phone_book) {
        for (let i = 1; i <= phoneNum.length; i++) {
            const prefix = phoneNum.slice(0, i);
            
            if (!count.has(prefix)) {
                count.set(prefix, 0);
            }
            
            count.set(prefix, count.get(prefix) + 1);
        }
    }
    
    // 접두사가 두 개 이상 존재하는지 확인
    let answer = true;
    
    for (const phoneNum of phone_book) {
        if (count.get(phoneNum) > 1) {
            answer = false;
            break;
        }
    }
    
    return answer;
}
function solution(s) {
    const numbers = [...s.split(' ')].map(Number);
    const min = Math.min(...numbers);
    const max = Math.max(...numbers);
    
    const answer = `${min} ${max}`;
    
    return answer;
}
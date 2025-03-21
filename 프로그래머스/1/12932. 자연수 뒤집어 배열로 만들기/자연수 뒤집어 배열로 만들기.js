function solution(n) {
    const answer = [...String(n)].map(Number);
    answer.reverse();
    
    return answer;
}
function solution(x, n) {
    const answer = [...Array(n).keys()].map((i) => x * (i + 1));
    
    return answer;
}
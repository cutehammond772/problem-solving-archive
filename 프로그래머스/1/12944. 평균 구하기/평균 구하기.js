function solution(arr) {
    const total = arr.reduce((sum, num) => sum + num, 0);
    const answer = total / arr.length;
    
    return answer;
}
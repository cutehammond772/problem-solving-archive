function solution(numbers) {
    const setOfNumbers = new Set(numbers);
    const allNumbers = [...Array(10).keys()];
    
    const answer = allNumbers
        .filter((num) => !setOfNumbers.has(num))
        .reduce((sum, num) => sum + num, 0);
    
    return answer;
}
function solution(n)
{
    const digits = [...String(n)].map((digit) => Number(digit));
    const answer = digits.reduce((sum, num) => num + sum, 0);

    return answer;
}
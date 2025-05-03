function solution(s) {
    const answer = s
        .split(' ')
        .map((word) => [...word.toLowerCase(), ''])
        .map(([first, ...last]) => [first.toUpperCase(), ...last].join(''))
        .join(' ');
    
    return answer;
}
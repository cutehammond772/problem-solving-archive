function solution(players, m, k) {
    let incrementServerCount = 0;
    let serverCount = 0;
    
    const hours = [...Array(24).keys()]
    const reservation = Array(24).fill(0)
    
    for (const hour of hours) {
        const currentPlayerCount = players[hour];
        
        // 증설한 Server를 반납합니다.
        serverCount -= reservation[hour];
        
        // Player 수를 Server가 감당할 수 있는지 체크합니다.
        if ((serverCount + 1) * m > currentPlayerCount)
            continue;
        
        const increment = Math.floor(currentPlayerCount / m) - serverCount;
        
        serverCount += increment;
        incrementServerCount += increment;
        
        if (hour + k < 24) {
            reservation[hour + k] += increment;
        }
    }
    
    const answer = incrementServerCount;
    
    return answer;
}
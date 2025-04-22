function solution(points, routes) {
    // 변수 초기화
    const queue = [];
    const [pointCount, robotCount] = [points.length, routes.length];
    
    // 로봇의 초기 위치 등록
    for (let i = 0; i < robotCount; i++) {
        const initialPoint = routes[i][0];
        
        // [time, robot, next, row, col]
        queue.unshift([0, i, 0, ...points[initialPoint - 1]]);
    }
    
    // 현재 시간
    let currentTime = 0;
    
    // 위험한 상황
    let dangerCount = 0;
    
    function updateDangerCount() {
        const map = [...Array(101).keys()].map(() => Array(101).fill(0));
        
        for (const [,,, row, col] of queue) {
            if (++map[row][col] === 2) {
                dangerCount++;
            }
        }
    }
    
    // 0초일 때 위험한 상황인지 체크
    updateDangerCount();
    
    while (queue.length > 0) {
        if (currentTime < queue[queue.length - 1][0]) {
            currentTime = queue[queue.length - 1][0];
            updateDangerCount();
        }
        
        let [time, robot, next, row, col] = queue.pop();
        
        // 해당 로봇의 다음 경로를 지정한다.
        let [nextRow, nextCol] = points[routes[robot][next] - 1];
        
        // 해당 포인트에 도착한 경우, 다음 포인트를 지정한다.
        if (nextRow === row && nextCol === col) {
            if (routes[robot].length === next + 1) continue;
            
            [nextRow, nextCol] = points[routes[robot][++next] - 1];
        }
        
        if (Math.abs(nextRow - row) > 0) {
            const dr = (nextRow - row) > 0 ? 1 : -1;
            queue.unshift([time + 1, robot, next, row + dr, col]);
        } else {
            const dc = (nextCol - col) > 0 ? 1 : -1;
            queue.unshift([time + 1, robot, next, row, col + dc]);
        }
    }
    
    return dangerCount;
}
function solution(n, w, num) {
    // 1. 층의 개수 (1~)
    const totalFloor = Math.ceil(n / w);
    
    // 2. num의 위치 (0 ~ (w - 1))
    const [floorOfNum, idxOfNum] = [Math.ceil(num / w), (num - 1) % w];
    
    // 2-1. 층이 맨 윗층이면 바로 꺼낼 수 있다.
    if (floorOfNum === totalFloor)
        return 1;
    
    // 3. 화살표의 방향은 홀수층이면 오른쪽, 짝수층이면 왼쪽이다.
    const idxFromLeft = (floorOfNum % 2 === 1) ? idxOfNum : ((w - 1) - idxOfNum);
    
    let addition;
    
    if (totalFloor % 2 === 1) {
        addition = (idxFromLeft > (n - 1) % w) ? 0 : 1;
    } else {
        addition = (idxFromLeft < (w - 1) - ((n - 1) % w)) ? 0 : 1;
    }
    
    const answer = (totalFloor - floorOfNum) + addition;
    
    return answer;
}
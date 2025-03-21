function solution(video_len, pos, op_start, op_end, commands) {
    function convertToNumber(s) {
        const [min, sec] = s.split(":").map(Number);
        
        return min * 60 + sec;
    }
    
    function convertToTimeString(time) {
        let [min, sec] = [Math.floor(time / 60), time % 60].map(String);
        
        if (min.length === 1)
            min = `0${min}`;
        
        if (sec.length === 1)
            sec = `0${sec}`;
        
        return `${min}:${sec}`;
    }
    
    const timeVideoLen = convertToNumber(video_len);
    const timePos = convertToNumber(pos);
    const timeOpStart = convertToNumber(op_start);
    const timeOpEnd = convertToNumber(op_end);
    
    let currentTime = timePos;
    
    // 1. 오프닝 구간 내에 있는지 확인
    function isInOpening(time) {
        return timeOpStart <= time && time <= timeOpEnd;
    }
    
    if (isInOpening(currentTime)) {
        currentTime = timeOpEnd;
    }
    
    // 2. 커맨드 처리
    for (const command of commands) {
        if (command === "prev") {
            currentTime = Math.max(0, currentTime - 10);
        } else if (command === "next") {
            currentTime = Math.min(timeVideoLen, currentTime + 10);
        }
        
        if (isInOpening(currentTime)) {
            currentTime = timeOpEnd;
        }
    }
    
    const answer = convertToTimeString(currentTime);
    
    return answer;
}
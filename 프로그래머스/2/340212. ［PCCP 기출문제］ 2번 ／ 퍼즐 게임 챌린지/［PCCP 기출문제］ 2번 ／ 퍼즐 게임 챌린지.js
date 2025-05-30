function isValid(diffs, times, limit, level) {
    const n = diffs.length;
    let total = 0;
    
    for (let i = 0; i < n; i++) {
        const [diff, time] = [diffs[i], times[i]];
        
        if (diff > level) {
            total += (diff - level) * (times[i - 1] + time) + time;
        } else {
            total += time;
        }
    }
    
    return total <= limit;
}

function solution(diffs, times, limit) {
    let left = 1, right = 100000;
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        
        if (isValid(diffs, times, limit, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    
    return right;
}
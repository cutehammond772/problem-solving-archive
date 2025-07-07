function solution(picks, minerals) {
    const [DIAMOND, IRON, STONE] = Array(3).keys();
    const dp = [...Array(6).keys()].map(() => [...Array(6).keys()].map(() => Array(6).fill(0)));
    
    let result = 2 ** 31 - 1;
    const maxPicks = picks[DIAMOND] + picks[IRON] + picks[STONE];
    const requiredPicks = Math.ceil(minerals.length / 5);
    
    // calculate cost
    const requiredCost = [];
    
    for (let i = 0; i < minerals.length; i++) {
        if (i % 5 === 0) {
            requiredCost.push([0, 0, 0]);
        }
        
        const last = requiredCost[requiredCost.length - 1];
        
        switch (minerals[i]) {
            case "diamond":
                last[DIAMOND] += 1;
                last[IRON] += 5;
                last[STONE] += 25;
                break;
                
            case "iron":
                last[DIAMOND] += 1;
                last[IRON] += 1;
                last[STONE] += 5;
                break;
                
            case "stone":
                last[DIAMOND] += 1;
                last[IRON] += 1;
                last[STONE] += 1;
                break;
        }
    }
    
    // resolve dp
    for (let x = 0; x <= picks[DIAMOND]; x++) {
        for (let y = 0; y <= picks[IRON]; y++) {
            for (let z = 0; z <= picks[STONE]; z++) {
                const totalUsedPicks = x + y + z;
                
                if (totalUsedPicks === 0 || requiredPicks < totalUsedPicks) {
                    continue;
                }
                
                const candidate = [];
                
                if (x > 0) {
                    candidate.push(dp[x - 1][y][z] + requiredCost[totalUsedPicks - 1][DIAMOND]);
                }
                if (y > 0) {
                    candidate.push(dp[x][y - 1][z] + requiredCost[totalUsedPicks - 1][IRON]);
                }
                if (z > 0) {
                    candidate.push(dp[x][y][z - 1] + requiredCost[totalUsedPicks - 1][STONE]);
                }
                
                
                dp[x][y][z] = Math.min(...candidate);
                
                if (totalUsedPicks >= Math.min(maxPicks, requiredPicks)) {
                    result = Math.min(result, dp[x][y][z]);
                }
            }
        }
    }
    
    return result;
}
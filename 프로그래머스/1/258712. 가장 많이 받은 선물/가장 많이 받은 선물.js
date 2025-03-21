function solution(friends, gifts) {    
    // 1. 모든 기록은 각 친구(friends)의 인덱스를 기준으로 한다.
    const countOfFriends = friends.length;
    
    const index = new Map(
        friends.map((friend, i) => [friend, i])
    );

    // 서로 간 선물을 주고받은 기록
    const giveInfo = [...Array(countOfFriends)]
        .map((_) => Array(countOfFriends).fill(0));
    
    // 한 사람이 선물을 주고 받은 횟수
    const giftCounts = Array(countOfFriends).fill(0);
    
    // 2. 선물 정보 등록
    gifts.map((info) => info.split(' '))
    .forEach(([a, b]) => {
        const aIdx = index.get(a);
        const bIdx = index.get(b);

        giveInfo[aIdx][bIdx] += 1;
        
        giftCounts[aIdx] += 1;
        giftCounts[bIdx] -= 1;
    });
    
    // 3. 정보 취합
    const range = [...Array(countOfFriends).keys()];
    const nextGiftCounts = Array(countOfFriends).fill(0);
    
    // (a, b) 매칭
    for (const a of range) {
        for (const b of range) {
            if (a >= b) continue;
            
            const aTob = giveInfo[a][b];
            const bToa = giveInfo[b][a];
            
            if (aTob === bToa) {
                if (giftCounts[a] > giftCounts[b])
                    nextGiftCounts[a] += 1;
                
                else if (giftCounts[a] < giftCounts[b])
                    nextGiftCounts[b] += 1;
                
                continue;
            }
            
            else if (aTob > bToa) {
                nextGiftCounts[a] += 1;
            }
            
            else {
                nextGiftCounts[b] += 1;
            }
        }
    }
    
    const answer = Math.max(...nextGiftCounts);
    
    return answer;
}
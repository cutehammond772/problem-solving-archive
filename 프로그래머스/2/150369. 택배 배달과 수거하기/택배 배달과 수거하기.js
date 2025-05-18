function solution(cap, n, deliveries, pickups) {
    // 최대한 왕복 거리를 줄이는 것이 핵심이다.
    // 따라서, 가장 먼 거리에 있는 집부터 배달 / 수거를 수행해야 한다.
    let totalDistance = 0;
    
    // 한 왕복 당 한 사이클로 생각한다.
    while (deliveries.length > 0 || pickups.length > 0) {
        // 현재 위치
        let deliveryIdx = deliveries.length - 1;
        let pickupIdx = pickups.length - 1;
        
        // 실제 이동 거리
        let deliveryDist = 0;
        let pickupDist = 0;
        
        // 누적 적재량
        let deliveryCap = 0;
        let pickupCap = 0;
        
        while (deliveries.length > 0 && deliveryCap < cap) {
            // 맨 끝에 아무 것도 배달할 게 없으면 제외시킨다.
            if (deliveries[deliveryIdx] === 0) {
                deliveries.pop();
                deliveryIdx -= 1;
                
                continue;
            }
            
            const delivery = Math.min(cap - deliveryCap, deliveries[deliveryIdx]);
            
            deliveryDist = Math.max(deliveryDist, deliveryIdx + 1);
            deliveryCap += delivery;
            deliveries[deliveryIdx] -= delivery;
        }
        
        while (pickups.length > 0 && pickupCap < cap) {
            // 맨 끝에 아무 것도 회수할 게 없으면 제외시킨다.
            if (pickups[pickupIdx] === 0) {
                pickups.pop();
                pickupIdx -= 1;
                
                continue;
            }
            
            const pickup = Math.min(cap - pickupCap, pickups[pickupIdx]);
            
            pickupDist = Math.max(pickupDist, pickupIdx + 1);
            pickupCap += pickup;
            pickups[pickupIdx] -= pickup;
        }
        
        totalDistance += Math.max(deliveryDist, pickupDist) * 2;
    }
    
    return totalDistance;
}
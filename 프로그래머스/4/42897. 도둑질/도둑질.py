def solution(money):
    # 첫번째 집을 마킹하는 경우
    memo1 = [0] * len(money)
    
    memo1[0] = memo1[1] = money[0]
    
    for x in range(2, len(money) - 1):
        memo1[x] = max(memo1[x - 2] + money[x], memo1[x - 1])
    
    memo1[-1] = memo1[-2]
        
    # 첫번째 집을 마킹하지 않는 경우
    memo2 = [0] * len(money)
    
    memo2[1] = money[1]
    
    for x in range(2, len(money)):
        memo2[x] = max(memo2[x - 2] + money[x], memo2[x - 1])
    
    return max(memo1[-1], memo2[-1])
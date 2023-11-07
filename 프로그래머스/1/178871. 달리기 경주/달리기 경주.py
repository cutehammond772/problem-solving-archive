def solution(players, callings):
    answer = players[:]
    
    # 선수와 위치(등수)를 대응시킵니다.
    ranks = dict()
    
    # 1. 기존 등수를 저장합니다. (0부터 시작)
    for rank in range(len(players)):
        ranks[players[rank]] = rank
    
    # 2. swap을 통해 선수의 추월을 반영합니다.
    for player in callings:
        rank = ranks[player] # 현재 추월하는 선수의 순위입니다.
        opposite = answer[rank - 1] # 추월당하는 상대입니다.
        
        answer[rank], answer[rank - 1] = answer[rank - 1], answer[rank]
        ranks[player], ranks[opposite] = ranks[opposite], ranks[player]
    
    return answer
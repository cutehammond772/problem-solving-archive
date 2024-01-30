def solution(name):
    # 알파벳을 바꾸는 데 필요한 조작 횟수
    change = 0
    
    for alphabet in name:
        change += min(ord(alphabet) - ord('A'), (ord('Z') - ord(alphabet)) + 1)
    
    if change == 0:
        return change
    
    # 'A'가 아닌 문자의 인덱스를 저장
    index = [x for x in range(len(name)) if name[x] != 'A']
    
    # 이동하는 데 필요한 조작 횟수
    move = min(max(index), len(name) - min(index))
    
    for i in range(len(index) - 1):
        x, y = index[i], index[i + 1]
        
        move = min(move, 2 * x + (len(name) - y), 2 * (len(name) - y) + x)
    
    return change + move
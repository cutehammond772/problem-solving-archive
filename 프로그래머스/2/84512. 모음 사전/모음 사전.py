# ((5 + 1) * 5 + 1) * 5
def solution(word):
    answer = 0
    memo = [781, 156, 31, 6, 1]
    character = ['A', 'E', 'I', 'O', 'U']
    
    for x in range(len(word)):
        answer += 1 + memo[x] * character.index(word[x])
    
    return answer
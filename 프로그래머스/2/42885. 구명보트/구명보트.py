def solution(people, limit):
    answer = 0
    people.sort()
    
    x, y = 0, len(people) - 1
    
    while x < y:
        answer += 1
        
        if people[x] + people[y] <= limit:
            x += 1
        
        y -= 1
    
    if x == y:
        answer += 1
    
    return answer
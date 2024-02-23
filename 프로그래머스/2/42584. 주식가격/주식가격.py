def solution(P):
    N = len(P)
    
    stack = []
    answer = [0] * N
    
    for y in range(N):
        while stack and P[stack[-1]] > P[y]:
            x = stack.pop()
            answer[x] = y - x
        
        stack.append(y)
    
    for i in range(len(stack)):
        x, y = stack[i], stack[-1]
        answer[x] = y - x
    
    return answer
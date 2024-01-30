def solution(number, k):
    stack = []
    
    # Decreasing Monotone Stack
    for x in range(len(number)):
        while k and stack and stack[-1] < number[x]:
            stack.pop()
            k -= 1
        
        stack.append(number[x])
    
    # k가 남았을 경우, 맨 끝부터 삭제한다.
    while k:
        stack.pop()
        k -= 1
    
    return "".join(stack)
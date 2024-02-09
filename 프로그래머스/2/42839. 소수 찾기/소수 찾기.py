from itertools import permutations

def check(x):
    if x < 2:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if not (x % i):
            return False
    
    return True

def solution(numbers):
    answer = 0
    discover = [False] * 10000000
    
    for size in range(1, len(numbers) + 1):
        for digits in permutations(numbers, size):
            num = int("".join(digits))
            
            if discover[num]:
                continue
            
            discover[num] = True
            answer += check(num)
    
    return answer
        
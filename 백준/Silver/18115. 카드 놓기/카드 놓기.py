import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	result = deque([])
	
	for num in range(1, N + 1):
		op = A.pop()
		
		if op == 1:
			result.appendleft(num)
		
		elif op == 2:
			first = result.popleft()
			
			result.appendleft(num)
			result.appendleft(first)
		
		elif op == 3:
			result.append(num)
	
	return result

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	print(*solve(N, A))
	
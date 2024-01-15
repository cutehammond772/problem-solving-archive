import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = 1001

def solve(N, A):
	memo = [INF] * N
	queue = deque([])
	
	queue.append(0)
	memo[0] = 0
	
	while queue:
		node = queue.popleft()
		
		for i in range(1, A[node] + 1):
			next = node + i
			
			if next >= N:
				continue
				
			if memo[node] + 1 >= memo[next]:
				continue
			
			memo[next] = memo[node] + 1
			queue.append(next)
	
	return memo[-1] if memo[-1] != INF else -1
	
if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]
	
	print(solve(N, A))
	
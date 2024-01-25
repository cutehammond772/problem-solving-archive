import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

# 날짜 역추적
def backtrack(N, M, G):
	result = deque([INF])
	temp = deque([])
	
	def traverse(p, q):
		nonlocal result
		
		if not G[p][q]:
			result = min(result, temp.copy())
			return
		
		for prev in G[p][q]:
			temp.appendleft(prev)
			traverse(prev, q - 1)
			temp.popleft()
	
	traverse(N, M)
	return result

def solve(N, M, P):
	# m번 청소했을 때, n일까지의 불쾌함의 총합의 최소
	memo = [[INF] * (M + 1) for _ in range(N + 1)]
	
	# p일 저녁에 청소하는 경우, q일까지의 불쾌함의 총합
	score = [[0] * (N + 1) for _ in range(N + 1)]
	
	# 해당 최소에서, 이전에 청소를 한 날짜
	previous = [[[] for _ in range(M + 1)] for _ in range(N + 1)]
	
	for p in range(N + 1):
		accumulation = 0
		total = 0
		
		for q in range(p + 1, N + 1):
			total += accumulation * P[q]
			score[p][q] = total
			
			accumulation += P[q]
	
	for n in range(1, N + 1):
		memo[n][0] = score[0][n]
		
		for i in range(1, n):
			for m in range(1, M + 1):
				candidate = memo[n - i][m - 1] + score[n - i][n]
				
				if memo[n][m] < candidate:
					continue
					
				if memo[n][m] > candidate:
					previous[n][m] = [n - i]
					memo[n][m] = candidate
				
				if memo[n][m] == candidate:
					previous[n][m].append(n - i)
	
	return memo[N][M], backtrack(N, M, previous)

if __name__ == "__main__":
	N, M = map(int, input().split())
	P = [0, *map(int, input().split())]
	score, days = solve(N, M, P)
	
	print(score)
	print(*days)
	
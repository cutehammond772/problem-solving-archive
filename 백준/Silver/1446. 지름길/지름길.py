import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10001

if __name__ == "__main__":
	N, D = map(int, input().split())
	
	memo = [INF] * (D + 1)
	path = [[] for _ in range(D + 1)]
	
	for _ in range(N):
		s, e, d = map(int, input().split())
		
		if e <= D:
			path[s].append((e, d))
	
	memo[0] = 0
	
	for s in range(D + 1):
		if s > 0:
			memo[s] = min(memo[s], memo[s - 1] + 1)
		
		for e, d in path[s]:
			memo[e] = min(memo[e], memo[s] + d)
	
	print(memo[D])
	
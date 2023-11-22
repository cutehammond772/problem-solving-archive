import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

if __name__ == '__main__':
	N, K = map(int, input().split())
	memo = [[0] * 3001 for _ in range(N)]
	
	for x in range(N):
		ai, bi = map(int, input().split())
		
		for y in range(ai, bi + 1):
			if x == 0:
				memo[x][y] = (memo[x][y - 1] + 1) % MOD
				
			else:
				memo[x][y] = (memo[x][y - 1]
				              + memo[x - 1][min(3000, y + K)]
				              - memo[x - 1][max(0, (y - 1) - K)]
				              ) % MOD
		
		for y in range(bi + 1, 3001):
			memo[x][y] = memo[x][bi]
	
	print(memo[-1][-1])
import sys
input = lambda: sys.stdin.readline().rstrip()

# dp[k][s] = max(dp[k - 1][s] + s, dp[k - 1][s - Bi] - Ai)
def solve(K, P):
	memo = [[-1] * 5001 for _ in range(K + 1)]
	
	# 초기 상태
	memo[0][1] = 0
	
	for k in range(1, K + 1):
		for s in range(1, 5001):
			# 1. 마우스를 클릭하고 당근을 s개 얻는다.
			if memo[k - 1][s] >= 0:
				memo[k][s] = max(memo[k][s], memo[k - 1][s] + s)
			
			# 2. 당근을 지불하여 스피드 효과를 구매한다.
			for Ai, Bi in P:
				if s > Bi and memo[k - 1][s - Bi] - Ai >= 0:
					memo[k][s] = max(memo[k][s], memo[k - 1][s - Bi] - Ai)
		
	return max(memo[K])

if __name__ == '__main__':
	N, K = map(int, input().split())
	P = []
	
	for _ in range(N):
		Ai, Bi = map(int, input().split())
		P.append((Ai, Bi))
	
	print(solve(K, P))
	
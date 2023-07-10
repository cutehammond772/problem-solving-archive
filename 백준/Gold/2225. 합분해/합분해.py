import sys

input = lambda: sys.stdin.readline().rstrip()
MOD = 1_000_000_000

def solve(N, K):
	# K번 더했을 때의 남은 수
	memo = [[0] * (N + 1) for _ in range(K + 1)]
	
	# 0~N까지의 수 1개를 더했을 경우
	memo[1] = [1] * (N + 1)
	
	for t in range(2, K + 1):
		for x in range(N + 1):
			for y in range(x, N + 1):
				memo[t][x] = (memo[t][x] + memo[t - 1][y]) % MOD
	
	return memo[K][0]
	
if __name__ == '__main__':
	N, K = map(int, input().split())
	print(solve(N, K))
	
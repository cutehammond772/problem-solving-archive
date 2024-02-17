import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 3)

def solve(N, K, init):
	memo = [[[0] * (K + 1) for _ in range(N + 1)] for _ in range(2)]
	
	# 첫번째 색깔의 선택 여부
	memo[0][1][0] = 1 - init
	memo[1][1][1] = init
		
	for n in range(2, N + 1):
		memo[0][n][0] = memo[0][n - 1][0]
		
		for k in range(1, K + 1):
			memo[0][n][k] = (memo[0][n - 1][k] + memo[1][n - 1][k]) % MOD
			memo[1][n][k] = memo[0][n - 1][k - 1]
	
	return memo

if __name__ == "__main__":
	N, K = int(input()), int(input())
	selected, unselected = solve(N, K, 1), solve(N, K, 0)
	
	print((selected[0][N][K] + unselected[1][N][K] + unselected[0][N][K]) % MOD)
	
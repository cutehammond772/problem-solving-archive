import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	memo = [[0] * 31 for _ in range(31)]
	
	for n in range(1, 31):
		memo[n][0] = 1
		
		for k in range(1, n + 1):
			memo[n][k] = memo[n - 1][k] + memo[n][k - 1]
	
	while N := int(input()):
		print(memo[N][N])
	
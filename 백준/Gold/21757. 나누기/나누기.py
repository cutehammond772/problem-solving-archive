import sys
input = lambda: sys.stdin.readline().rstrip()

# dp[n][k] = dp[n - 1][k]
def solve(N, A):
	total = sum(A)
	
	# 4등분으로 나눌 수 있는 경우가 없다.
	if total % 4:
		return 0
	
	memo = [[0] * 4 for _ in range(N)]
	target = total >> 2
	
	for i in range(1, N):
		A[i] += A[i - 1]
	
	for i in range(N):
		if i > 0:
			memo[i][1] = memo[i - 1][1]
		
		if A[i] == target:
			memo[i][1] += 1
	
	for j in range(2, 4):
		for i in range(1, N):
			memo[i][j] = memo[i - 1][j]
			
			if i >= j - 1 and A[i] == target * j:
				memo[i][j] += memo[i - 1][j - 1]
	
	return memo[-2][3]

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	print(solve(N, A))
	
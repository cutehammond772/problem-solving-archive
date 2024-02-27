import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

# DP with Knuth Optimization
def solve(N, S):
	C = [0] * (N + 1)
	M = [[INF] * (N + 1) for _ in range(N + 2)]
	A = [[0] * (N + 1) for _ in range(N + 2)]
	
	# C[x...y] = C[y] - C[x - 1]
	for i in range(1, N + 1):
		C[i] = S[i] + C[i - 1]
	
	# 파일 하나의 경우 비용이 필요하지 않다.
	for i in range(1, N + 1):
		M[i][i], A[i][i] = 0, i
	
	for s in range(2, N + 1):
		for i in range(1, (N + 2) - s):
			j = (i + s) - 1
			
			# 사각 부등식의 성질을 통해 k의 범위를 좁히는 것이 핵심이다.
			for k in range(A[i][j - 1], A[i + 1][j] + 1):
				cost = M[i][k] + M[k + 1][j] + (C[j] - C[i - 1])
				
				if M[i][j] > cost:
					M[i][j], A[i][j] = cost, k
	
	return M[1][N]

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		S = [0, *map(int, input().split())]
		
		print(solve(N, S))
	
import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, D, T):
	memo = [[False] * (M + 1) for _ in range(N + 1)]
	memo[0][0] = True
	
	for i in range(N):
		curr = i + 1
		
		for j in range(D[i]):
			for num in range(M, T[i][j] - 1, -1):
				memo[curr][num] |= (memo[curr - 1][num - T[i][j]] | memo[curr][num - T[i][j]])
	
	for num in range(M, -1, -1):
		if memo[N][num]:
			return num
	
	return -1

if __name__ == '__main__':
	N, M = map(int, input().split())
	D = [*map(int, input().split())]
	T = [[*map(int, input().split())] for _ in range(N)]
	
	print(solve(N, M, D, T))
	
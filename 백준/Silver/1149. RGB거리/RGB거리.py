import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, D):
	memo = [[0] * 3 for _ in range(N + 1)]
	
	for x in range(1, N + 1):
		for k in range(3):
			memo[x][k] = min(memo[x - 1][(k + 1) % 3], memo[x - 1][(k + 2) % 3]) + D[x - 1][k]
	
	return min(memo[N])

if __name__ == "__main__":
	N = int(input())
	D = [[*map(int, input().split())] for _ in range(N)]
	
	print(solve(N, D))
	
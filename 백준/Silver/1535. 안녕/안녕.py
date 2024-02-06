import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, L, J):
	memo = [-1] * 100
	memo[0] = 0
	
	for x in range(N):
		for i in range(99, L[x] - 1, -1):
			memo[i] = max(memo[i], memo[i - L[x]] + J[x])
	
	return max(memo)

if __name__ == "__main__":
	N = int(input())
	L = [*map(int, input().split())]
	J = [*map(int, input().split())]
	
	print(solve(N, L, J))

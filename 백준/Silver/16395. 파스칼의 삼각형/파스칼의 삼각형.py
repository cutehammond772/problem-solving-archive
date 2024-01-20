import sys, math
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K):
	return math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

if __name__ == '__main__':
	N, K = map(int, input().split())
	print(solve(N - 1, K - 1))
	
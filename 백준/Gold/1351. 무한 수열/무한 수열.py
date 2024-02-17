import sys
input = lambda: sys.stdin.readline().rstrip()

# top-down approach
def solve(N, P, Q):
	memo = dict()
	memo[0] = 1
	
	def a(i):
		if i not in memo:
			memo[i] = a(i // P) + a(i // Q)
		
		return memo[i]
	
	return a(N)

if __name__ == "__main__":
	N, P, Q = map(int, input().split())
	print(solve(N, P, Q))
	
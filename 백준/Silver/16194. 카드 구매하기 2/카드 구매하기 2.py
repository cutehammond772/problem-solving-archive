import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, sequence):
	memo = [0] + sequence
	
	for x in range(1, N + 1):
		for y in range(1, x + 1):
			memo[x] = min(memo[x], memo[y] + memo[x - y])
			
	return memo[N]
	
if __name__ == '__main__':
	N = int(input())
	sequence = [*map(int, input().split())]
	
	print(solve(N, sequence))
	
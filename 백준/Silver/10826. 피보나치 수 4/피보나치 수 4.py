import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	memo = [0, 1]
	
	for _ in range(2, N + 1):
		memo.append(memo[-1] + memo[-2])
	
	return memo[N]

if __name__ == '__main__':
	N = int(input())
	print(solve(N))
	
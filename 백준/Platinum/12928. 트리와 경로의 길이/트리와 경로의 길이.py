import sys
input = lambda: sys.stdin.readline().rstrip()

def calc(x):
	return x * (x + 1) // 2

def solve(N, S):
	if N < 3:
		return 0
	
	# memo[1 ... N-2]
	memo = [[False] * (S + 1) for _ in range(N - 1)]
	
	# x = 1 ... N - 2
	for x in range(1, N - 1):
		if calc(x) <= S:
			memo[x][calc(x)] = True
		
		for y in range(1, (x // 2) + 1):
			A, B = memo[y], memo[x - y]
			
			for i in range(1, S + 1):
				for j in range(1, S + 1):
					if i + j > S:
						break
						
					memo[x][i + j] |= A[i] and B[j]
	
	return int(memo[N - 2][S])

if __name__ == '__main__':
	N, S = map(int, input().split())
	print(solve(N, S))
	
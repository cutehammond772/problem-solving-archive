import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(D, K):
	memo = [[0, 0], [1, 0], [0, 1]]
	
	while len(memo) <= D:
		memo.append([memo[-2][0] + memo[-1][0], memo[-2][1] + memo[-1][1]])
	
	a, b = memo[D]
	
	for x in range(1, 50001):
		by = K - a * x
		
		if by % b:
			continue
		
		return x, by // b

if __name__ == "__main__":
	D, K = map(int, input().split())
	print(*solve(D, K), sep='\n')
	
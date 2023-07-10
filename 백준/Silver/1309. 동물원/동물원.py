import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 9901

def solve(N):
	memo = []
	
	# [empty, left, right]
	memo.append([1, 1, 1])
	
	for _ in range(1, N):
		total = sum(memo[-1])
		
		memo.append([
			total % MOD,
			(total - memo[-1][1]) % MOD,
			(total - memo[-1][2]) % MOD
		])
	
	return sum(memo[-1]) % MOD

if __name__ == '__main__':
	N = int(input())
	print(solve(N))
		
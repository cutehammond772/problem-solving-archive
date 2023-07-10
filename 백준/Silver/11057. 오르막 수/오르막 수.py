import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10007

def solve(N):
	memo = [1] * 10
	
	for _ in range(1, N):
		next = [0] * 10
		
		for x in range(10):
			for y in range(x, 10):
				next[y] += memo[x]
				
		memo = [x % MOD for x in next]
		
	return sum(memo) % MOD
	
if __name__ == '__main__':
	N = int(input())
	print(solve(N))
		
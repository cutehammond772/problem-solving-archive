import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 1_000_000_009

def preprocess():
	memo = [0] * 1000001
	memo[1], memo[2], memo[3] = 1, 2, 4
	
	for x in range(4, 1000001):
		memo[x] = (memo[x - 1] + memo[x - 2] + memo[x - 3]) % MOD
	
	return memo

if __name__ == '__main__':
	T = int(input())
	memo = preprocess()
	
	for _ in range(T):
		N = int(input())
		print(memo[N])
		
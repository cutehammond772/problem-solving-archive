import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 1_000_000_009

def preprocess():
	# last added: [0, 1, 2, 3]
	memo = [[0] * 4 for _ in range(100001)]
	
	memo[1] = [1, 1, 0, 0]
	memo[2] = [1, 0, 1, 0]
	memo[3] = [3, 1, 1, 1]
	
	for x in range(4, 100001):
		memo[x][1] = (memo[x - 1][2] + memo[x - 1][3]) % MOD
		memo[x][2] = (memo[x - 2][1] + memo[x - 2][3]) % MOD
		memo[x][3] = (memo[x - 3][1] + memo[x - 3][2]) % MOD
		
		memo[x][0] = (memo[x][1] + memo[x][2] + memo[x][3]) % MOD
		
	return memo
	
if __name__ == '__main__':
	T = int(input())
	memo = preprocess()
	
	for _ in range(T):
		N = int(input())
		print(memo[N][0])
	
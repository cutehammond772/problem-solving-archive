import sys, math
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 6

def solve(N):
	L = len(N)
	memo = [0] * L

	for x in range(L):
		# 맨 끝 한 자리에 대한 유효성 확인
		one = int(N[x])

		if 0 < one < 10:
			if x == 0:
				memo[x] += 1
			else:
				memo[x] = (memo[x] + memo[x - 1]) % MOD

		# 맨 끝 두 자리에 대한 유효성 확인
		if x > 0:
			two = int(N[x - 1]) * 10 + one

			if 10 <= two <= 26:
				if x < 2:
					memo[x] = (memo[x] + 1) % MOD
				else:
					memo[x] = (memo[x] + memo[x - 2]) % MOD

	return memo[L - 1]

if __name__ == "__main__":
	N = input()
	print(solve(N))

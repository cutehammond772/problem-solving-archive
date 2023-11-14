import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

def factorials(N):
	result = [1]

	for x in range(1, N + 1):
		result.append((result[-1] * x) % MOD)

	return result

def pow(a, x):
	result = 1

	while x:
		if x & 1:
			result = (result * a) % MOD

		a = (a * a) % MOD
		x >>= 1

	return result

# nCm = n!/(m!(n - m)!)
def solve(N, M):
	f = factorials(N)

	return (f[N] * pow(f[M], MOD - 2) * pow(f[N - M], MOD - 2)) % MOD

if __name__ == '__main__':
	N, M = map(int, input().split())
	print(solve(N, M))

import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

f = [1] * 100001

for x in range(2, 100001):
	f[x] = (x * f[x - 1]) % MOD

def comb(n, r):
	return (f[n] * pow(f[n - r], MOD - 2, MOD) * pow(f[r], MOD - 2, MOD)) % MOD

# H가 "홀수 개" 있어야 게임을 승리할 수 있다.
def solve(S):
	result = 0
	p, q = S.count("?"), S.count("H")
	
	# H가 홀수 개인 경우에 사용된 ?의 개수
	candidate = [x - q for x in range(q, (p + q) + 1) if x % 2]
	
	# sum(pCr)
	for r in candidate:
		result = (result + comb(p, r)) % MOD
	
	return result

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		N = input()
		print(solve(N))
		
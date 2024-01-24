import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
MOD = 998_244_353

def factorials(N):
	result = [1] * (N + 1)
	
	for x in range(2, N + 1):
		result[x] = (result[x - 1] * x) % MOD
	
	return result

def pow(P, Q):
	result = 1
	
	while Q:
		if Q & 1:
			result = (result * P) % MOD
		
		Q >>= 1
		P = (P * P) % MOD
	
	return result

# 0! ... 1000000!
f = factorials(1_000_000)

def comb(N, R):
	return (f[N] * pow(f[R], MOD - 2) * pow(f[N - R], MOD - 2)) % MOD

# 아이디어: 집합 내 "원소"에 중점을 둔다.
# 특정 원소에 대해, 해당 원소가 존재하는 집합 내에서 (k개를) 골라야만 교집합의 원소에 등장하게 된다.
# 따라서, 모든 집합에 대해 등장하는 각 원소에 대해 조합을 구한 후 각각 더한다.
# ex. "1"이 포함된 집합이 3개이면, NC1 ... NC3에서 각각 3C1 ... 3C3을 더하면 된다.
def solve(N, S):
	# NC1 ... NCN
	result = [0] * (N + 1)
	elements = defaultdict(int)
	
	for i in range(N):
		for element in S[i]:
			elements[element] += 1
	
	for A in elements.values():
		for B in range(1, A + 1):
			result[B] = (result[B] + comb(A, B)) % MOD
	
	return result[1:]

if __name__ == "__main__":
	N = int(input())
	S = []
	
	for _ in range(N):
		P, *Q = map(int, input().split())
		S.append(Q)
	
	print(*solve(N, S), sep='\n')
	
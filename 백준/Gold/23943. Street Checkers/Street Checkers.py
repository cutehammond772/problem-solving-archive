import sys
input = lambda: sys.stdin.readline().rstrip()

def preprocess(N):
	N = int(N ** 0.5) + 1
	check = [True] * N

	check[0] = False
	check[1] = False

	for i in range(2, int(N ** 0.5) + 1):
		if not check[i]:
			continue

		for n in range(i << 1, N, i):
			check[n] = False

	return [x for x in range(N) if check[x]]

def check(P, X):
	for prime in P:
		if X <= prime:
			return 1

		if not X % prime:
			return 0

	return 1

# 2가 0개 : 짝수가 0개이므로 나머지 수는 "소수"여야 한다.
# 2가 1개 : 짝수와 홀수의 개수는 무조건 같으므로 0 => 무조건 성립
# 2가 2개 : 나머지 수는 무조건 소수 (또는 1)여야 한다.
# 2가 3개 : 8만 성립한다.
# 2가 4개 이상 : 불가능
def resolve(P, x):
	if not (x % (2 ** 3)):
		return 1 if x == 8 else 0

	if not (x % (2 ** 2)):
		return check(P, x >> 2)

	if not (x % (2 ** 1)):
		return 1

	return check(P, x)

if __name__ == '__main__':
	T = int(input())
	P = preprocess(10 ** 9)

	for i in range(1, T + 1):
		L, R = map(int, input().split())
		result = 0

		for t in range(L, R + 1):
			result += resolve(P, t)

		print(f"Case #{i}: {result}")

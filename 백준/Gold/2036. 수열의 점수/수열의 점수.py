import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(NP, P):
	NP.sort(reverse=True)
	P.sort()

	result = 0

	# 0 + (음수)의 경우, 최대한 짝지어서 곱하는 것이 이득이다.
	while NP:
		if len(NP) == 1:
			result += NP.pop()
			continue

		result += NP.pop() * NP.pop()

	# (양수)의 경우,
	# 2 이상과 짝지어질 경우: 곱하는 게 이득
	# 1과 짝지어질 경우: 더하는 게 이득
	while P:
		if len(P) == 1:
			result += P.pop()
			continue

		x, y = P.pop(), P.pop()

		if y == 1:
			result += (x + y)
		else:
			result += x * y

	return result

if __name__ == "__main__":
	N = int(input())

	# non-positives, positives
	NP, P = [], []

	for _ in range(N):
		X = int(input())

		if X > 0: P.append(X)
		else: NP.append(X)

	print(solve(NP, P))

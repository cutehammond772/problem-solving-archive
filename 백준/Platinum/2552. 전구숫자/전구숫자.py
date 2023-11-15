import sys, math
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
	x, y = 0, len(A)

	while x < y:
		mid = (x + y) >> 1

		if A[mid][0] >= K:
			y = mid

		else:
			x = mid + 1

	return x

def solve(N, B, K):
	high, low = B[:(N // 2)][::-1], B[(N // 2):][::-1]
	H, L = len(high), len(low)

	high_matches, low_matches = [], []

	for bit in range(1 << H):
		first = last = N + 1
		possible = True

		for i in range(H):
			if not (bit & 1 << i):
				continue

			if high[i] > first:
				possible = False
				break

			if last == N + 1:
				last = high[i]

			first = high[i]

		if possible:
			high_matches.append((bit, last if bit else 0))

	for bit in range(1 << L):
		first, possible = N + 1, True

		for i in range(L):
			if not (bit & 1 << i):
				continue

			if low[i] > first:
				possible = False
				break

			first = low[i]

		if possible:
			low_matches.append((first, bit))

	check = 1
	high_matches.sort()
	low_matches.sort()

	LM = len(low_matches)

	for bit, last in high_matches:
		size = LM - lower_bound(low_matches, last + 1)

		if check <= K < check + size:
			candidate = [bit for first, bit in low_matches[LM - size:]]
			candidate.sort()
			return candidate[K - check] + (bit << L)

		check += size

	return -1

if __name__ == '__main__':
	N = int(input())
	B = [*map(int, input().split())]
	K = int(input())

	print(solve(N, B, K))

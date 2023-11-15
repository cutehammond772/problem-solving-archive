import sys
input = lambda: sys.stdin.readline().rstrip()

def find(A, K):
	x, y = 0, len(A) - 1

	while x <= y:
		mid = (x + y) >> 1

		if A[mid][0] == K:
			return (True, A[mid][1])

		if A[mid][0] > K:
			y = mid - 1

		else:
			x = mid + 1

	return (False, 0)

def convert(left, right, L, R):
	result = []

	for i in range(L):
		result.append("1" if left & 1 << i else "0")

	for i in range(R):
		result.append("1" if right & 1 << i else "0")

	return "".join(result)

def solve(N, A, K):
	left, right = A[:(N // 2)], A[(N // 2):]
	L, R = len(left), len(right)

	left_combs, right_combs = [], []

	for bit in range(1 << L):
		result = 0

		for i in range(L):
			if bit & 1 << i:
				result += left[i]

		left_combs.append((result, bit))

	for bit in range(1 << R):
		result = 0

		for i in range(R):
			if bit & 1 << i:
				result += right[i]

		right_combs.append((result, bit))

	right_combs.sort()

	for left_sum, left_bit in left_combs:
		if left_sum > K:
			continue

		has, right_bit = find(right_combs, K - left_sum)

		if has:
			return convert(left_bit, right_bit, L, R)

	return -1

if __name__ == '__main__':
	N = int(input())
	A = [int(input()) for _ in range(N)]
	K = int(input())

	print(solve(N, A, K))

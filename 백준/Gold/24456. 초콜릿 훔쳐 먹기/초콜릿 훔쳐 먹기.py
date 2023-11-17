import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, K):
	diff = abs(N - M)
	current = N * M

	while current > 1:
		num = current - 1
		next_diff = -1

		for div in range(1, int(num ** 0.5) + 1):
			if num % div:
				continue

			candidate = (num // div) - div

			if candidate > K:
				continue

			next_diff = candidate
			break

		if next_diff < 0:
			break

		if next_diff == num - 1:
			current = 1
			break

		current = num
		diff = next_diff

	return N * M - current

if __name__ == '__main__':
	N, M, K = map(int, input().split())
	print(solve(N, M, K))

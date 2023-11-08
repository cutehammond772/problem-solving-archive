import sys
input = lambda: sys.stdin.readline().rstrip()

def resolve(x):
	# [even, odd]
	result = [0, 0]

	for i in range(1, int(x ** 0.5) + 1):
		if not x % i:
			p, q = i, x // i

			result[p % 2] += 1

			if p != q:
				result[q % 2] += 1

	return result

if __name__ == '__main__':
	T = int(input())
	memo = dict()

	for i in range(1, T + 1):
		L, R = map(int, input().split())
		result = 0

		for t in range(L, R + 1):
			if t in memo:
				result += memo[t]
				continue

			even, odd = resolve(t)
			memo[t] = 1 if abs(even - odd) <= 2 else 0

			result += memo[t]

		print(f"Case #{i}: {result}")

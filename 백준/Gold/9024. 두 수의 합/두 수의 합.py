import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		N, K = map(int, input().split())
		Q = [*map(int, input().split())]

		x, y = 0, N - 1
		num, count = INF, 0
		Q.sort()

		while x < y:
			t = Q[x] + Q[y]

			if abs(K - t) < abs(K - num):
				num = t
				count = 1

			elif abs(K - t) == abs(K - num):
				count += 1

			if K >= t:
				x += 1
			else:
				y -= 1

		print(count)

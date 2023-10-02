import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 2 ** 63 - 1

def solve(N, T, P, D):
	# 각 마을마다 두 칸의 비트필드를 갖는다.
	# 이는, 각 마을과 연결된 쌍둥이 마을의 수를 나타낸다.
	memo = [INF] * (2 ** (N * 2))
	memo[0] = 0

	def dist(d1, d2):
		x1, y1 = T[d1]
		x2, y2 = T[d2]

		return abs(x1 - x2) + abs(y1 - y2)

	def get_candidate(x):
		result = []

		for p in range(x):
			dist_p = dist(x, p)

			if dist_p < D:
				continue

			result.append([dist_p, p])

			if P >= 2:
				for q in range(p + 1, x):
					dist_q = dist(x, q)

					if dist_q < D:
						continue

					result.append([dist_p + dist_q, p, q])

					if P >= 3:
						for r in range(q + 1, x):
							dist_r = dist(x, r)

							if dist_r < D:
								continue

							result.append([dist_p + dist_q + dist_r, p, q, r])

		return result

	def convert_slot(bit, x):
		result = []

		for _ in range(x):
			result.append(bit % 4)
			bit >>= 2

		return result

	def convert_bit(slot):
		result = 0

		for num in slot[::-1]:
			result <<= 2
			result += num

		return result

	def counts(bit):
		result = 0

		while bit:
			result += bit % 4
			bit >>= 2

		return result

	# 첫번째 마을부터 순회하되,
	# 지금까지 순회한 마을끼리만 쌍둥이 마을을 만들 수 있는 경우의 수를 만들도록 한다.
	for x in range(1, N):
		candidate = get_candidate(x)

		for bit in range(2 ** (x * 2)):
			if memo[bit] == INF:
				continue

			default_slot = convert_slot(bit, x)

			for distance, *selections in candidate:
				slot = default_slot[:]
				valid = True

				for idx in selections:
					if slot[idx] + 1 > P:
						valid = False
						break

					slot[idx] += 1

				if not valid:
					continue

				slot.append(len(selections))
				next_bit = convert_bit(slot)

				memo[next_bit] = min(memo[next_bit], memo[bit] + distance)

	result = (0, 0)

	for bit in range(2 ** (N * 2)):
		if memo[bit] != INF:
			count, distance = counts(bit) // 2, memo[bit]
			result = max(result, (count, -distance))

	return result[0], -result[1]

if __name__ == "__main__":
	N = int(input())
	T = []

	for _ in range(N):
		x, y = map(int, input().split())
		T.append((x, y))

	P, D = map(int, input().split())

	print(*solve(N, T, P, D))

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	result = [['A'] * N for _ in range(7)]
	last_level = 0

	def resolve(level, x, y):
		nonlocal last_level
		mid = (x + y) // 2

		if y - x <= 1:
			return

		last_level = max(last_level, level)
		result[level][mid:y] = ['B'] * (y - mid)

		resolve(level + 1, x, mid)
		resolve(level + 1, mid, y)

	resolve(0, 0, N)

	# 남는 경기에 대해, 최소한의 조건을 만족시키도록 함
	for x in range(last_level + 1, 7):
		result[x][0] = 'B'

	return result

if __name__ == "__main__":
	N = int(input())
	result = solve(N)

	for sequence in result:
		print("".join(sequence))

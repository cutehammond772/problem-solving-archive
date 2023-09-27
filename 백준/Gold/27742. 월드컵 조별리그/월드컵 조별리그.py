import sys
input = lambda: sys.stdin.readline().rstrip()

INF = 10 ** 12 + 1
POINT, GOAL_DIFF, GOALS = 0, 1, 2

def solve(T, K, board, unknown):
	def check():
		totals = [[0] * 3 + [4 - i] for i in range(4)]

		for x in range(3):
			for y in range(x + 1, 4):
				score_xy, score_yx = board[x][y], board[y][x]

				if score_xy > score_yx:
					totals[x][POINT] += 3
				elif score_yx > score_xy:
					totals[y][POINT] += 3
				else:
					totals[x][POINT] += 1
					totals[y][POINT] += 1

				totals[x][GOAL_DIFF] += score_xy - score_yx
				totals[y][GOAL_DIFF] += score_yx - score_xy

				totals[x][GOALS] += score_xy
				totals[y][GOALS] += score_yx

		totals.sort(reverse=True)

		for rank in range(4):
			if totals[rank][3] == 4 - T:
				return rank < 2

		return False

	result = INF
	low, high = 0, K
	a, b = unknown

	while low <= high:
		mid = (low + high) // 2
		board[a][b] = mid

		if check():
			result = min(result, mid)
			high = mid - 1
		else:
			low = mid + 1

	return result if result != INF else -1

if __name__ == "__main__":
	T, K = map(int, input().split())

	board = [[0] * 4 for _ in range(4)]
	unknown = None

	for row in range(4):
		data = [*map(int, input().split())]

		for col in range(4):
			if data[col] == -1:
				unknown = (row, col)
				continue

			board[row][col] = data[col]

	print(solve(T - 1, K, board, unknown))

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N, Q = map(int, input().split())

	rows, cols = [True] * (N + 1), [True] * (N + 1)
	row_count, col_count = 0, 0
	row_discount, col_discount = 0, 0

	for _ in range(Q):
		A, B = input().split()
		B = int(B)

		if A == 'R':
			if not rows[B]:
				print(0)

			else:
				result = 0

				# 삭제된 COLUMN 반영
				result += B * (N - col_count)
				result += (N * (N + 1) // 2) - col_discount
				print(result)

				# ROW 삭제
				rows[B] = False
				row_count += 1
				row_discount += B

		if A == 'C':
			if not cols[B]:
				print(0)

			else:
				result = 0

				# 삭제된 ROW 반영
				result += B * (N - row_count)
				result += (N * (N + 1) // 2) - row_discount
				print(result)

				# COLUMN 삭제
				cols[B] = False
				col_count += 1
				col_discount += B

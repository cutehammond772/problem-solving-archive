import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(rows, cols, K):
	result = 0

	rows.sort()
	cols.sort()

	R, C = len(rows), len(cols)
	r_off, c_off = R - 1, 0

	while r_off >= 0 and c_off < C:
		area = rows[r_off] * cols[c_off]

		if area <= K:
			result += r_off + 1
			c_off += 1
			continue

		r_off -= 1

	return result

if __name__ == '__main__':
	W, H, K = map(int, input().split())
	N, R = int(input()), [0, *map(int, input().split()), H]
	M, C = int(input()), [0, *map(int, input().split()), W]

	# 가로, 세로 구간 전처리
	r_off, c_off = 1, 1
	rows, cols = [], []

	while r_off <= N + 1:
		rows.append(R[r_off] - R[r_off - 1])
		r_off += 1

	while c_off <= M + 1:
		cols.append(C[c_off] - C[c_off - 1])
		c_off += 1

	print(solve(rows, cols, K))

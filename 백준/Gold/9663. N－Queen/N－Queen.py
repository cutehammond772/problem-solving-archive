import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	# 총 경우의 수이다.
	result = 0

	# 경우의 수를 따지는 데 사용된다.
	cols = [False] * N
	queens = []

	def check(row):
		nonlocal result

		# 행의 인덱스가 N까지 왔다는 것은 퀸이 모두 배치된 것과 같다.
		if row == N:
			result += 1
			return

		for col in range(N):
			if cols[col]:
				continue

			# 대각선 체크
			cross = False

			for qr, qc in queens:
				if abs(qr - row) == abs(qc - col):
					cross = True
					break

			if cross:
				continue

			cols[col] = True
			queens.append((row, col))

			check(row + 1)

			cols[col] = False
			queens.pop()

	# 퀸을 N개 놓기 위해서는, 모든 행에 퀸을 배치해야 한다.
	# 즉, 0번째 행부터 무조건 놓아야 한다.
	check(0)

	return result

if __name__ == "__main__":
	N = int(input())
	print(solve(N))

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N, M = map(int, input().split())
	mx = [input().split() for _ in range(N)]

	# ceil((a * b + 1) / 2) : 과반수 초과
	# -> 동일한 이름이 적힌 칸이 "2x1 or 3x1"에 두 개 존재하는 경우를 찾는다.
	names = set()

	for row in range(N):
		for col in range(M):
			check = False

			# 1 x 2
			check |= col + 1 < M and mx[row][col] == mx[row][col + 1]

			# 1 x 3
			check |= col + 2 < M and mx[row][col] == mx[row][col + 2]

			# 2 x 1
			check |= row + 1 < N and mx[row][col] == mx[row + 1][col]

			# 3 x 1
			check |= row + 2 < N and mx[row][col] == mx[row + 2][col]

			if check:
				names.add(mx[row][col])

	if names:
		print(*sorted(names), sep='\n')
	else:
		print("MANIPULATED")

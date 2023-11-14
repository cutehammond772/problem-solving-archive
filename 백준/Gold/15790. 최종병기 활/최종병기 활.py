import sys
input = lambda: sys.stdin.readline().rstrip()

# "최소 고무줄의 길이"의 최대를 구한다.
def solve(N, M, X, K):
	x, y = 1, 100001

	# Parametric Search
	while x < y:
		length = (x + y) // 2
		possible = False

		# 처음으로 자르는 위치를 정한다.
		for offset in range(M):
			accumulation = 0
			count = 0

			X.append(N + X[offset])

			for i in range(offset, M):
				accumulation += X[i + 1] - X[i]

				if accumulation >= length:
					accumulation = 0
					count += 1

			X.pop()

			if count >= K:
				possible = True
				break

		if possible:
			x = length + 1
		else:
			y = length

	result = x - 1
	return result if result else -1

if __name__ == '__main__':
	N, M, K = map(int, input().split())
	X = [int(input()) for _ in range(M)]

	print(solve(N, M, X, K))

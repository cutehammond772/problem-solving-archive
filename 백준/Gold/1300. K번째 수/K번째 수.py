import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K):
	x, y = 1, N * N

	# B[K]보다 작거나 같은 수가 최소 K개 존재한다.
	while x <= y:
		mid = (x + y) // 2

		count = 0
		for t in range(1, N + 1):
			count += min(mid // t, N)

		# 이분 탐색을 통해 특정 값을 찾아간다.
		if count >= K:
			y = mid - 1
		else:
			x = mid + 1

	return x

if __name__ == "__main__":
	N, K = int(input()), int(input())
	print(solve(N, K))

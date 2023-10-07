import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
INF = 1000001

# 거리값이 홀수이면 DAY, 짝수이면 NIGHT로 생각할 수 있다.
if __name__ == "__main__":
	N, M, K = map(int, input().split())
	walls = [[int(x) for x in input()] for _ in range(N)]

	memo = [[[INF] * (K + 1) for _ in range(M)] for _ in range(N)]
	queue = deque([])

	# 시작 지점에 대한 초기 설정
	queue.append((0, 0, 0, 1))

	for x in range(K + 1):
		memo[0][0][x] = 1

	while queue:
		row, col, wall, dist = queue.popleft()

		if (row, col) == (N - 1, M - 1):
			continue

		if memo[row][col][wall] < dist:
			continue

		if memo[N - 1][M - 1][wall] <= dist + ((N - 1) - row) + ((M - 1) - col):
			continue

		for x in range(4):
			nrow, ncol, nwall, ndist = row + dr[x], col + dc[x], wall, dist + 1

			if not (0 <= nrow < N and 0 <= ncol < M):
				continue

			if walls[nrow][ncol]:
				# 이미 K개의 벽을 깬 상태라면 넘어간다.
				if nwall + 1 > K:
					continue

				# 지금 NIGHT(=거리값이 짝수)라면 거리 1만큼 더 기다린다.
				if not dist % 2:
					ndist += 1

				nwall += 1

			if memo[nrow][ncol][nwall] <= ndist:
				continue

			for w in range(nwall, K + 1):
				if memo[nrow][ncol][w] <= ndist:
					break

				memo[nrow][ncol][w] = ndist

			queue.append((nrow, ncol, nwall, ndist))

	result = memo[N - 1][M - 1][K]
	print(result if result < INF else -1)

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, T):
	# 본인 세포의 크기
	cell = 2

	# (질량이) 가장 큰 세포가 되는 데 필요한 시간
	time = 0

	i = 0
	T.sort()

	# 먹을 수 있는 세포들
	edible = []

	while i < N:
		while i < N and cell > T[i]:
			edible.append(T[i])
			i += 1

		# 세포가 가장 큰 세포가 된 경우 (같은 경우 포함)
		if cell >= T[-1]:
			return time

		# 위의 경우를 제외하면, 더이상 먹을 수 없을 때 가장 큰 세포에 도달할 수 없다.
		if not edible:
			return "NIE"

		cell += edible.pop()
		time += 1

	# 모든 세포를 먹을 수 있으면 가장 큰 세포이다.
	return time

if __name__ == "__main__":
	N = int(input())
	T = [*map(int, input().split())]

	print(solve(N, T))

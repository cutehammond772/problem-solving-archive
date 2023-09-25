import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	result = 0
	schedules = []
	start, end = 0, 0

	# 문제 규칙대로 정렬한다.
	A.sort()

	for x in range(N):
		S, E = A[x][0], -A[x][1]

		# 일정을 처음 배치할 때
		if not schedules:
			schedules = [(S, E)]
			start, end = S, E
			continue

		# 서로 완전히 떨어뜨릴 수 있는 경우 코팅지 영역을 분리할 수 있다.
		if (end + 1) < S:
			result += len(schedules) * (end - start + 1)

			schedules = [(S, E)]
			start, end = S, E
			continue

		# 기존 일정에 추가된 여부를 확인한다.
		added = False

		# 최대한 상단에 배치한다.
		for x in range(len(schedules)):
			sx, ex = schedules[x]

			if ex < S:
				schedules[x] = (sx, E)
				end = max(end, E)
				added = True
				break

		if not added:
			schedules.append((S, E))
			end = max(end, E)

	result += len(schedules) * (end - start + 1)
	return result

if __name__ == "__main__":
	N = int(input())
	A = []

	for _ in range(N):
		S, E = map(int, input().split())
		A.append((S, -E))

	print(solve(N, A))

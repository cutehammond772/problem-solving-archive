import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, D, students, algorithms):
	# 특정 실력차 구간을 유지하기 위해 실력 오름차순으로 정렬한다.
	students.sort()
	x = 0

	# 해당 알고리즘을 알고 있는 학생의 수이다.
	check = [0] * (K + 1)
	algo_count, stud_count, result = 0, 0, 0

	# (1) 모든 학생들이 알아야 효율성이 줄어든다. 즉 학생을 최대한 많이 잡는 것이 이득이다.
	# (2) 효율성에 대해 별도로 따질 필요가 없는 이유는,
	# 특정 알고리즘에 대해 모든 학생들이 알고 있는 경우 누구를 배제시킨다 해도
	# 나머지 학생들 또한 모두 알고 있기 때문이다. (이득 X)
	for y in range(N):
		dx, ix = students[x]
		dy, iy = students[y]

		# 1. y번째 학생을 그룹에 포함시킨다.
		for alg in algorithms[iy]:
			if not check[alg]:
				algo_count += 1

			check[alg] += 1

		stud_count += 1

		# 2. 항상 실력차가 D 이하가 되도록 유지한다.
		while dy - dx > D:
			for alg in algorithms[ix]:
				check[alg] -= 1

				if not check[alg]:
					algo_count -= 1

			stud_count -= 1
			x += 1

			dx, ix = students[x]

		result = max(result, stud_count * (algo_count - check.count(stud_count)))

	return result

if __name__ == "__main__":
	N, K, D = map(int, input().split())
	students = []
	algorithms = []

	for x in range(N):
		M, d = map(int, input().split())
		A = [*map(int, input().split())]

		students.append((d, x))
		algorithms.append(A)

	print(solve(N, K, D, students, algorithms))

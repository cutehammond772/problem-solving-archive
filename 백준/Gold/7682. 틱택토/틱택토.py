import sys
input = lambda: sys.stdin.readline().rstrip()

O, X = 0, 1
cases = {
	(0, 1, 2), (3, 4, 5), (6, 7, 8),
	(0, 3, 6), (1, 4, 7), (2, 5, 8),
	(0, 4, 8), (2, 4, 6)
}
mapper = {'O': O, 'X': X, '.': 2}

def convert(case):
	counts = [0, 0, 0]
	matrix = [0] * 9

	for x in range(9):
		type = mapper[case[x]]

		counts[type] += 1
		matrix[x] = type

	return counts, matrix

def check(matrix):
	result = [0, 0]

	for p, q, r in cases:
		if matrix[p] == matrix[q] == matrix[r]:
			# .인 경우는 제외한다.
			if matrix[p] < 2:
				result[matrix[p]] += 1

	return tuple(result)

def solve(counts, matrix):
	# (조건 1.) X의 개수는 O의 개수보다 항상 같거나 크다.
	if counts[X] < counts[O]:
		return "invalid"

	# (조건 2.) X와 O의 차이는 1 또는 0이다.
	if counts[X] - counts[O] > 1:
		return "invalid"

	# (조건 3.) X의 개수는 6을 넘을 수 없다. (=> (X, O)는 (5, 4)가 최대이다.)
	if counts[X] > 5:
		return "invalid"

	total = check(matrix)

	# (조건 4.) X와 O가 각각 한 줄씩 성립하면 유효하지 않다.
	if total == (1, 1):
		return "invalid"

	# (조건 5.) 어떤 것도 한 줄 이상이 성립하지 않을 때, 꽉 찬 상태가 아니면 유효하지 않다.
	if total == (0, 0) and (counts[X] + counts[O]) < 9:
		return "invalid"

	# (조건 6.) O가 한 줄이 성립할 때, X는 O보다 더 클 수 없다.
	if total == (1, 0) and counts[X] > counts[O]:
		return "invalid"

	# (조건 7.) X가 한 줄이 성립할 때, O는 X의 개수와 같을 수 없다.
	if total == (0, 1) and counts[X] == counts[O]:
		return "invalid"

	return "valid"

if __name__ == "__main__":
	# 'end'를 입력받을 때까지 계속 테스트 케이스를 받는다.
	while (case := input()) != "end":
		counts, matrix = convert(case)
		print(solve(counts, matrix))

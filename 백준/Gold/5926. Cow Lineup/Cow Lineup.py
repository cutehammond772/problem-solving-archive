import sys
input = lambda: sys.stdin.readline().rstrip()

def compress(N, A):
	result = []
	breeds, indexes = set(), {}

	for i in range(N):
		x, b = A[i]

		if b not in breeds:
			indexes[b] = len(breeds)
			breeds.add(b)

		result.append((x, indexes[b]))

	return result, len(breeds)

def sweep(N, T, S):
	check, count = [0] * S, 0
	x, y = 0, 0

	# 오른쪽으로 쓸어가면서 종을 모두 포함시킬 때까지 이동한다.
	while y < N:
		tb = T[y][1]

		if not check[tb]:
			count += 1

		check[tb] += 1

		if count >= S:
			break

		y += 1

	while x < y:
		tb = T[x][1]

		# 이 종이 하나만 남았으면 그 이상 이동할 수 없다.
		if check[tb] <= 1:
			break

		check[tb] -= 1
		x += 1

	return abs(T[y][0] - T[x][0])

def solve(N, A):
	# 종의 종류를 압축시킨다.
	T, spec = compress(N, A)

	# 좌표 순서대로 정렬한다.
	T.sort()

	# 왼쪽에서 오른쪽으로 쓸어가면서 확인한다.
	left = sweep(N, T, spec)

	# 오른쪽에서 왼쪽으로 쓸어가면서 확인한다.
	right = sweep(N, T[::-1], spec)

	return min(left, right)

if __name__ == "__main__":
	N = int(input())
	A = []

	for _ in range(N):
		x, b = map(int, input().split())
		A.append((x, b))

	print(solve(N, A))

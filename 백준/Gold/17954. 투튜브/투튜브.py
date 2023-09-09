import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	if N == 1:
		return 2, [[1], [2]]

	T = N * 2

	# Example (N = 5)
	# 7 / (654 / 8)
	# 9 / (321 / 10)

	R = N - 2
	R1, R2 = 1, (T - 4) // 2 + 1

	A1, B1 = [T - 3], [T - 1]
	A2, B2 = [*range(R2, R2 + R)][::-1], [*range(R1, R1 + R)][::-1]
	A3, B3 = [T - 2], [T]

	rot = 0
	arr = [A1 + A2 + A3, B1 + B2 + B3]

	# 사과가 나오는 순서이다.
	order = A1 + A2 + A3 + B1 + B2 + B3
	accu = sum(order)

	for t in range(2 * N):
		rot += accu * t
		accu -= order[t]

	return rot, arr

if __name__ == "__main__":
	N = int(input())
	rot, arr = solve(N)

	print(rot)
	print(*arr[0])
	print(*arr[1])

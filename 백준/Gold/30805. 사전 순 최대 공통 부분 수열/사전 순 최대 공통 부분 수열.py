import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, A, B):
	# 인덱싱
	a_index = [[] for _ in range(101)]
	b_index = [[] for _ in range(101)]

	for i in range(N):
		a_index[A[i]].append(i)

	for i in range(M):
		b_index[B[i]].append(i)

	result = []
	a_off = b_off = -1

	for num in range(100, 0, -1):
		# 둘 다 존재하지 않으면 넘어간다.
		if not (a_index[num] and b_index[num]):
			continue

		ax = bx = 0

		while ax < len(a_index[num]):
			if a_index[num][ax] > a_off:
				break

			ax += 1

		while bx < len(b_index[num]):
			if b_index[num][bx] > b_off:
				break

			bx += 1

		size = min(len(a_index[num]) - ax, len(b_index[num]) - bx)
		
		if size > 0:
			result.extend([num] * size)
	
			a_off = a_index[num][ax + size - 1]
			b_off = b_index[num][bx + size - 1]

	return result

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]

	M = int(input())
	B = [*map(int, input().split())]

	result = solve(N, M, A, B)

	print(len(result))

	if result:
		print(*result)

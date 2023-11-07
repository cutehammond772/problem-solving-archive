import sys
input = lambda: sys.stdin.readline().rstrip()

def find(total):
	x, y = 0, 10 ** 20

	while x < y:
		t = (x + y) // 2

		if t * (t + 1) // 2 <= total:
			x = t + 1
		else:
			y = t

	return x - 1

def solve(N, M, L, A):
	x, y = 0, 10 ** 20

	# 성향 아이템 전처리
	for i in range(N):
		total = A[i] + ((L[i] - 1) * L[i] // 2)
		A[i] = find(total) - L[i] + 1

	while x < y:
		target = (x + y) // 2
		possible = True
		remain = M

		for i in range(N):
			total = L[i] + A[i]

			if total >= target:
				continue

			remain -= target - total

			if remain < 0:
				possible = False
				break

		if possible:
			x = target + 1

		else:
			y = target

	result = x - 1
	return -1 if result < max(L) else result

if __name__ == '__main__':
	N, M = map(int, input().split())

	L = [*map(int, input().split())]
	A = [*map(int, input().split())]

	print(solve(N, M, L, A))

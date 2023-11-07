import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 18

# K >= 1 + ... + N으로부터 N의 최대를 구한다.
def find(K):
	x, y = 0, INF

	while x < y:
		t = (x + y) // 2

		if t * (t + 1) // 2 <= K:
			x = t + 1
		else:
			y = t

	return x - 1

def solve(N, M, L, A):
	x, y = 0, INF

	# 1. 성향 아이템으로 올릴 수 있는 "레벨 단위"로 변환한다.
	for i in range(N):
		# (x + 1) 레벨을 올리기 위해 x개의 아이템이 필요하므로,
		# 1 + ... + (x - 1) + A[i] = 1 + ... + R에서
		# R - (X - 1)을 계산함으로써 레벨을 역산할 수 있다.
		total = A[i] + ((L[i] - 1) * L[i] // 2)
		A[i] = find(total) - (L[i] - 1)

	# 2. Parametric Search를 이용하여 최대 다각형을 구한다.
	while x < y:
		target = (x + y) // 2
		possible = True

		# 어떤 성향에든 사용할 수 있는 (남은) 비약이다.
		remain = M

		for i in range(N):
			total = L[i] + A[i]

			# 비약 없이도 특정 레벨을 올릴 수 있는 경우이다.
			if total >= target:
				continue

			remain -= target - total

			# 비약이 모자라면 이 레벨에 도달하는 것은 불가능하다.
			if remain < 0:
				possible = False
				break

		if possible:
			x = target + 1

		else:
			y = target

	result = x - 1

	# 결과가 기존 성향의 최대 레벨에 도달하지 못한 경우
	# 정다각형을 만드는 것은 불가능하다.
	return -1 if result < max(L) else result

if __name__ == '__main__':
	N, M = map(int, input().split())

	L = [*map(int, input().split())]
	A = [*map(int, input().split())]

	print(solve(N, M, L, A))

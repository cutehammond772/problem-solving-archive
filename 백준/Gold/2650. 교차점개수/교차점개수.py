import sys
input = lambda: sys.stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
	result = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
	return 1 if result > 0 else -1 if result < 0 else 0

def intersects(x1, y1, x2, y2, x3, y3, x4, y4):
	Q1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
	Q2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

	# 한 직선 위에 존재할 때
	if Q1 == Q2 == 0:
		if (x1, y1) > (x2, y2):
			x1, x2 = x2, x1
			y1, y2 = y2, y1

		if (x3, y3) > (x4, y4):
			x3, x4 = x4, x3
			y3, y4 = y4, y3

		# 최소 교차 조건
		C0 = (x3, y3) <= (x2, y2) and (x1, y1) <= (x4, y4)

		# 포함 관계 X
		C1 = (x1, y1) <= (x3, y3) and (x4, y4) <= (x2, y2)
		C2 = (x3, y3) <= (x1, y1) and (x2, y2) <= (x4, y4)

		return C0 and not (C1 or C2)

	return Q1 <= 0 and Q2 <= 0

def convert(P, X):
	if P == 1:
		return X, 50

	if P == 2:
		return X, 0

	if P == 3:
		return 0, 50 - X

	if P == 4:
		return 50, 50 - X

	# 이 이외의 경우는 존재하지 않는다.

def solve(N, lines):
	total = 0
	intersections = [0] * N

	if N < 2:
		return 0, 0

	for x in range(N - 1):
		for y in range(x + 1, N):
			if intersects(*lines[x], *lines[y]):
				total += 1
				intersections[x] += 1
				intersections[y] += 1

	return total, max(intersections)

if __name__ == "__main__":
	N = int(input())
	lines = []

	N //= 2

	for _ in range(N):
		P1, X1, P2, X2 = map(int, input().split())
		lines.append([*convert(P1, X1), *convert(P2, X2)])

	total, max_intersection = solve(N, lines)
	print(total)
	print(max_intersection)

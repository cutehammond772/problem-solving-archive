import sys
from math import sqrt
input = lambda: sys.stdin.readline().rstrip()

def solve(A, B, C):
	A2, B2, C2 = A ** 2, B ** 2, C ** 2
	E = (A2 - B2 + C2) / (C * 2)

	return (C * sqrt(A2 - (E ** 2))) / sqrt(B2 + C * E - C2 * 3 / 4)

if __name__ == "__main__":
	N = int(input())
	result = 0.0

	for _ in range(N):
		A, B, C = map(int, input().split())
		result += solve(float(A), float(B), float(C))

	print(result)

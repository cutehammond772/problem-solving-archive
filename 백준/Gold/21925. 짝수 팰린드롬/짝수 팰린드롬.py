import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, Q):
	result, x = 0, 0

	for y in range(1, N, 2):
		if Q[x] != Q[y]:
			continue

		correct = True

		for z in range(1, (y - x - 1) // 2 + 1):
			if Q[x + z] != Q[y - z]:
				correct = False
				break

		if correct:
			result += 1
			x = y + 1

	if x != N:
		return -1

	return result

if __name__ == "__main__":
	N = int(input())
	Q = [*map(int, input().split())]

	print(solve(N, Q))

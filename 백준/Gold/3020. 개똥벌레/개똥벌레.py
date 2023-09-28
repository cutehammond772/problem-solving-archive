import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 200001

# IMOS Trick
def solve(H, walls):
	result, count = INF, 0
	current = 0

	for x in range(H):
		current += walls[x]

		if result == current:
			count += 1
		elif result > current:
			result, count = current, 1

	return result, count

if __name__ == "__main__":
	N, H = map(int, input().split())
	walls = [0] * H

	for x in range(N):
		K = int(input())

		# 석순
		if x % 2:
			walls[H - K] += 1

		# 종유석
		else:
			walls[0] += 1
			walls[K] -= 1

	print(*solve(H, walls))

import sys
input = lambda: sys.stdin.readline().rstrip()

# 각 수로부터 3과 2가 곱해진 횟수를 추출한다.
def solve(N, B):
	analysis = []

	for i in range(N):
		current = B[i]
		three, two = 0, 0

		while not (current % 3):
			current //= 3
			three += 1

		while not (current % 2):
			current //= 2
			two += 1

		analysis.append((-three, two, B[i]))

	analysis.sort()

	return [analysis[x][2] for x in range(N)]

if __name__ == "__main__":
	N = int(input())
	B = [*map(int, input().split())]

	print(*solve(N, B))

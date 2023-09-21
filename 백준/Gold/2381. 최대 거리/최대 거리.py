import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N = int(input())
	ADD, SUB = [], []

	for _ in range(N):
		x, y = map(int, input().split())

		ADD.append(x + y)
		SUB.append(x - y)

	ADD.sort()
	SUB.sort()

	print(max(ADD[-1] - ADD[0], SUB[-1] - SUB[0]))

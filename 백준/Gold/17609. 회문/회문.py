import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(S, x, y):
	while x <= y:
		if S[x] == S[y]:
			x += 1
			y -= 1
			continue

		if S[x + 1] == S[y]:
			if solve(S, x + 1, y) == 0:
				return 1

		if S[x] == S[y - 1]:
			if solve(S, x, y - 1) == 0:
				return 1

		return 2

	return 0

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		S = input()
		print(solve(S, 0, len(S) - 1))

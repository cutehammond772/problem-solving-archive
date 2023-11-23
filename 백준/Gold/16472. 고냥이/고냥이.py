import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, S):
	count, result = 0, 0
	x, y = 0, 0

	check = [0] * 26

	while x <= y < len(S):
		if not check[S[y]]:
			count += 1

		check[S[y]] += 1

		while count > N:
			check[S[x]] -= 1

			if not check[S[x]]:
				count -= 1

			x += 1

		result = max(result, y - x + 1)
		y += 1

	return result

if __name__ == '__main__':
	N = int(input())
	S = [ord(ch) - ord('a') for ch in input()]

	print(solve(N, S))

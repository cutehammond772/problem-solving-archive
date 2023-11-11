import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(S, Q, queries):
	result = []
	memo = [[0] * len(S) for _ in range(26)]

	for x in range(len(S)):
		a = ord(S[x]) - ord('a')

		for y in range(26):
			if x > 0:
				memo[y][x] = memo[y][x - 1]

			if a == y:
				memo[y][x] += 1

	for a, l, r in queries:
		a = ord(a) - ord('a')

		if l > 0:
			result.append(memo[a][r] - memo[a][l - 1])
		else:
			result.append(memo[a][r])

	return result

if __name__ == '__main__':
	S = input()
	Q = int(input())
	queries = []

	for _ in range(Q):
		a, l, r = input().split()
		queries.append((a, int(l), int(r)))

	result = solve(S, Q, queries)
	print(*result, sep='\n')

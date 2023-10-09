import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(X, N):
	memo, visit = [X], {X}

	for t in range(N):
		if memo[-1] % 2:
			memo.append((memo[-1] << 1) ^ 6)
		else:
			memo.append((memo[-1] >> 1) ^ 6)

		if memo[-1] in visit:
			start = memo.index(memo[-1], 0, len(memo) - 1)
			sequence = (len(memo) - 1) - start

			return memo[start + (N - start) % sequence]

		visit.add(memo[-1])

	return memo[-1]

if __name__ == "__main__":
	X, N = map(int, input().split())
	print(solve(X, N))

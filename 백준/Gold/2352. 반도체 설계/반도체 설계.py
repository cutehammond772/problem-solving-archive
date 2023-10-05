import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
	x, y = 0, len(A)

	while x < y:
		mid = (x + y) // 2

		if A[mid] >= K:
			y = mid
		else:
			x = mid + 1

	return x

# LIS
def solve(N, Q):
	sequence = []

	for x in range(N):
		num = Q[x]

		if not sequence or sequence[-1] < num:
			sequence.append(num)
			continue
		
		sequence[lower_bound(sequence, num)] = num

	return len(sequence)

if __name__ == "__main__":
	N = int(input())
	Q = [*map(int, input().split())]

	print(solve(N, Q))

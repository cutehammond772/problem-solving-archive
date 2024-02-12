import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	for sequence in permutations(range(1, N + 1)):
		check = [0] * N
		
		for x in range(N):
			for y in range(x):
				check[sequence[x] - 1] += sequence[y] > sequence[x]
		
		if tuple(A) == tuple(check):
			return sequence
	
	return None

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	print(*solve(N, A))
		
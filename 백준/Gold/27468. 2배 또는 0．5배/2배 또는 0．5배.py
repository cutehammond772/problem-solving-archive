import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	sequence = [*range(1, N + 1)]
	offset = 3 if N % 4 == 2 else 2
	
	for x in range(offset, N, 4):
		sequence[x - 1], sequence[x] = sequence[x], sequence[x - 1]
	
	return sequence

if __name__ == '__main__':
	N = int(input())
	sequence = solve(N)
		
	print("YES")
	print(*sequence)

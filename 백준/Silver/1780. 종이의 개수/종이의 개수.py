import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def check(data, N, M, size):
	result = [0] * 3
	
	for row in range(N, N + size):
		for col in range(M, M + size):
			result[data[row][col] + 1] |= 1
	
	return result

def solve(data, N, M, size):
	A, B, C = check(data, N, M, size)
	
	if [A, B, C].count(0) == 2:
		return A, B, C
	
	A = B = C = 0
	k = size // 3
	
	for x in range(3):
		for y in range(3):
			p, q, r = solve(data, N + (k * x), M + (k * y), k)
			A += p; B += q; C += r
	
	return A, B, C

if __name__ == "__main__":
	N = int(input())
	data = [[*map(int, input().split())] for _ in range(N)]
	
	A, B, C = solve(data, 0, 0, N)
	print(A, B, C, sep='\n')
	
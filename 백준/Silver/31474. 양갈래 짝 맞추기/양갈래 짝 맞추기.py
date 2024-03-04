import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	f = [1] * 29

	for x in range(2, 29):
		f[x] = x * f[x - 1]
		
	result = 1
	group = 0
	
	while N:
		result *= f[N] // (f[2] * f[N - 2])
		group += 1
		
		N -= 2
	
	return result // f[group]

if __name__ == '__main__':
	N = int(input())
	print(solve(N))
	
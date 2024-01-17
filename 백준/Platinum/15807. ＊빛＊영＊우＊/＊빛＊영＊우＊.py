import sys
input = lambda: sys.stdin.readline().rstrip()
OFF = 1500

if __name__ == '__main__':
	memo = [[0] * 3001 for _ in range(3002)]
	
	N = int(input())
	
	for _ in range(N):
		xi, yi = map(int, input().split())
		
		for k in range(yi, 1501):
			p, q = max(-1500, xi + (yi - k)), min(1500, xi + (k - yi))
			
			memo[OFF + p][OFF + k] += 1
			memo[OFF + q + 1][OFF + k] += -1
	
	for y in range(3001):
		for x in range(1, 3001):
			memo[x][y] += memo[x - 1][y]
	
	P = int(input())
	
	for _ in range(P):
		xpi, ypi = map(int, input().split())
		print(memo[OFF + xpi][OFF + ypi])
		
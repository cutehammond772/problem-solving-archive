import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, stickers):
	# [empty, up, down]
	memo = [0, stickers[0][0], stickers[1][0]]
	
	for x in range(1, N):
		memo = [
			max(memo),
			stickers[0][x] + max(memo[0], memo[2]),
			stickers[1][x] + max(memo[0], memo[1]),
		]
		
	return max(memo)

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		stickers = [[*map(int, input().split())] for _ in range(2)]
		
		print(solve(N, stickers))
		
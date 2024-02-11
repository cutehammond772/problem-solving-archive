import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(H, W, A):
	result = 0
	
	for h in range(H):
		streak = -1
		
		for w in range(W):
			if A[w] - 1 < h:
				streak += streak >= 0
			else:
				result += max(0, streak)
				streak = 0
	
	return result

if __name__ == "__main__":
	H, W = map(int, input().split())
	A = [*map(int, input().split())]
	
	print(solve(H, W, A))
	
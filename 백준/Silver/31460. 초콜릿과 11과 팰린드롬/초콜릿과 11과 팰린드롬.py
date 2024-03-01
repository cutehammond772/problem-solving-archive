import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	if N < 4:
		return [0, 0, 11, 121][N]
	
	return "11" + ("0" * (N - 4)) + "11"

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		print(solve(N))
		
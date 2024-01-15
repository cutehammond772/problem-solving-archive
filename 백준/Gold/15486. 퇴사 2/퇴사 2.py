import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	memo = [0] * (N + 1)
	
	for start in range(N):
		T, P = A[start]
		end = start + T
		
		memo[start] = max(memo[start], memo[start - 1])
		
		if end <= N:
			memo[end] = max(memo[end], memo[start] + P)
	
	return max(memo[N - 1], memo[N])

if __name__ == '__main__':
	N = int(input())
	A = []
	
	for _ in range(N):
		T, P = map(int, input().split())
		A.append((T, P))
	
	print(solve(N, A))
	
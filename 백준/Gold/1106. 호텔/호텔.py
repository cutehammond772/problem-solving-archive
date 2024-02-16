import sys, math
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def solve(C, A):
	memo = [INF] * (C + 1)
	memo[0] = 0
	
	for P, Q in A:
		for x in range(C):
			for i in range(1, math.ceil((C - x) / Q) + 1):
				memo[min(x + Q * i, C)] = min(memo[min(x + Q * i, C)], memo[x] + P * i)
	
	return memo[C]
	
if __name__ == "__main__":
	C, N = map(int, input().split())
	A = []
	
	for _ in range(N):
		P, Q = map(int, input().split())
		A.append((P, Q))
	
	print(solve(C, A))
	
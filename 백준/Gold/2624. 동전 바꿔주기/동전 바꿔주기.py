import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(T, S):
	memo = [0] * (T + 1)
	
	# 처음에는 0원인 경우만 존재
	memo[0] = 1
	
	for P, N in S:
		for x in range(T - P, -1, -1):
			if not memo[x]:
				continue
			
			for i in range(1, N + 1):
				if x + P * i > T:
					break
					
				memo[x + P * i] += memo[x]
	
	return memo[T]

if __name__ == "__main__":
	T, K = int(input()), int(input())
	S = []
	
	for _ in range(K):
		P, N = map(int, input().split())
		S.append((P, N))
	
	print(solve(T, S))
	
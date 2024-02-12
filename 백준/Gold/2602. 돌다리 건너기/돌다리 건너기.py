import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(S, A, B):
	N, L = len(S), len(A)
	
	dpA = [[0] * (N + 1) for _ in range(L + 1)]
	dpB = [[0] * (N + 1) for _ in range(L + 1)]
	
	# 시작점
	for i in range(1, L + 1):
		dpA[i][1] = dpA[i - 1][1]
		dpB[i][1] = dpB[i - 1][1]
		
		if S[0] == A[i - 1]:
			dpA[i][1] += 1
		
		if S[0] == B[i - 1]:
			dpB[i][1] += 1
	
	for k in range(2, N + 1):
		for i in range(1, L + 1):
			dpA[i][k] = dpA[i - 1][k]
			dpB[i][k] = dpB[i - 1][k]
			
			if S[k - 1] == A[i - 1]:
				dpA[i][k] += dpB[i - 1][k - 1]
			
			if S[k - 1] == B[i - 1]:
				dpB[i][k] += dpA[i - 1][k - 1]
	
	return dpA[L][N] + dpB[L][N]

if __name__ == "__main__":
	S = input()
	A, B = [*input()], [*input()]
	
	print(solve(S, A, B))
	
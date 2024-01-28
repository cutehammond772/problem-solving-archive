import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(P, Q, R):
	LP, LQ, LR = len(P), len(Q), len(R)
	memo = [[[0] * (LR + 1) for _ in range(LQ + 1)] for _ in range(LP + 1)]
	
	for p in range(1, LP + 1):
		for q in range(1, LQ + 1):
			for r in range(1, LR + 1):
				memo[p][q][r] = max(memo[p - 1][q][r], memo[p][q - 1][r], memo[p][q][r - 1])
				
				if P[p - 1] == Q[q - 1] == R[r - 1]:
					memo[p][q][r] = max(memo[p][q][r], memo[p - 1][q - 1][r - 1] + 1)
	
	return memo[LP][LQ][LR]

if __name__ == "__main__":
	P, Q, R = input(), input(), input()
	print(solve(P, Q, R))
	
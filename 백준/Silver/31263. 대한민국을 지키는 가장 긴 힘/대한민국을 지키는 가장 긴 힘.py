import sys
input = lambda: sys.stdin.readline().rstrip()

def valid(*digits):
	number = 0
	
	for i in range(len(digits)):
		if i == 0 and digits[i] == 0:
			return False
		
		number = number * 10 + digits[i]
	
	return 1 <= number <= 641

def solve(N, A):
	memo = [N] * (N + 1)
	memo[0] = 0
	
	for x in range(1, N + 1):
		if valid(A[x]):
			memo[x] = min(memo[x], memo[x - 1] + 1)
		
		if x > 1 and valid(A[x - 1], A[x]):
			memo[x] = min(memo[x], memo[x - 2] + 1)
		
		if x > 2 and valid(A[x - 2], A[x - 1], A[x]):
			memo[x] = min(memo[x], memo[x - 3] + 1)
	
	return memo[N]

if __name__ == "__main__":
	N = int(input())
	A = [0] + [int(ch) for ch in input()]
	
	print(solve(N, A))
	
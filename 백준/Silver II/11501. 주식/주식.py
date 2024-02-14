import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	memo = [*A, 0]
	stack = []
	
	for x in range(N):
		# 누적 합
		if x > 0:
			memo[x] += memo[x - 1]
		
		while stack and A[stack[-1]] <= A[x]:
			stack.pop()
		
		stack.append(x)
	
	result, offset = 0, -1
	
	for x in stack:
		result += (A[x] * (x - offset)) - (memo[x] - memo[offset])
		offset = x
	
	return result

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		A = [*map(int, input().split())]
		
		print(solve(N, A))
		
import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
	A.sort()
	stack = []
	
	for p, q in A:
		while stack and stack[-1] < q:
			stack.pop()
		
		stack.append(q)
	
	return len(stack)

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		A = []
		
		for _ in range(N):
			P, Q = map(int, input().split())
			A.append((N - P, N - Q))
			
		print(solve(A))
			
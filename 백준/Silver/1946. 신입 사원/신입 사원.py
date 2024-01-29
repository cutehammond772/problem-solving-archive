import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	count = 0
	rank = N
	
	A.sort()
	
	for p, q in A:
		if rank < q:
			continue
		
		count += 1
		rank = q
	
	return count

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		A = []
		
		for _ in range(N):
			P, Q = map(int, input().split())
			A.append((P, Q))
			
		print(solve(N, A))
			
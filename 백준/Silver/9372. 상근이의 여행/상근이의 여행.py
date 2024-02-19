import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N, M = map(int, input().split())
		E = []
		
		for _ in range(M):
			a, b = map(int, input().split())
			E.append((a, b))
		
		print(N - 1)
	
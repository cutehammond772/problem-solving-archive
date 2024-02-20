import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	sequence = []
	
	def traverse(X):
		if X == 0:
			print(*sequence)
			return
		
		L = X if not sequence else sequence[-1]
	
		for i in range(min(X, L), 0, -1):
			sequence.append(i)
			traverse(X - i)
			sequence.pop()
		
	traverse(N)

if __name__ == "__main__":
	N = int(input())
	solve(N)
	
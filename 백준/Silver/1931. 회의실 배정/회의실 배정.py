import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
	count = 0
	end = 0
	
	A.sort()
	
	for y, x in A:
		if end <= x:
			count += 1
			end = y
	
	return count

if __name__ == "__main__":
	N = int(input())
	A = []
	
	for _ in range(N):
		x, y = map(int, input().split())
		A.append((y, x))
	
	print(solve(A))
	
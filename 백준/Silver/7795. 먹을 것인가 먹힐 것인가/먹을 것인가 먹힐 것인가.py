import sys
input = lambda: sys.stdin.readline().rstrip()

def find(A, K):
	x, y = 0, len(A)
	
	while x < y:
		mid = (x + y) >> 1
		
		if A[mid] >= K:
			y = mid
		
		else:
			x = mid + 1
	
	return x

def solve(A, B):
	result = 0
	
	# A 내림차순, B 오름차순
	A.sort(reverse=True)
	B.sort()
	
	for num in A:
		result += find(B, num)
	
	return result

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N, M = map(int, input().split())
		
		A = [*map(int, input().split())]
		B = [*map(int, input().split())]
		
		print(solve(A, B))
	
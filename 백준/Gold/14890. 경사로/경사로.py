import sys
input = lambda: sys.stdin.readline().rstrip()

def check(N, L, A):
	count = [0] * N
	streak = 0
	
	# uphill
	for x in range(1, N):
		diff = A[x - 1] - A[x]
		
		if diff > 1:
			return False
		
		if diff == 0 and streak:
			count[x] += 1
			streak += 1
		
		else:
			if streak > 0:
				return False
			
			if diff == 1:
				count[x] += 1
				streak = 1
			
		if streak == L:
			streak = 0
	
	if streak > 0:
		return False
	
	# downhill
	for x in range(N - 2, -1, -1):
		diff = A[x + 1] - A[x]
		
		if diff > 1:
			return False
		
		if diff == 0 and streak:
			count[x] += 1
			streak += 1
		
		else:
			if streak > 0:
				return False
			
			if diff == 1:
				count[x] += 1
				streak = 1
		
		if streak == L:
			streak = 0
			
	if streak > 0:
		return False
	
	return count.count(2) == 0

def solve(N, L, data):
	result = 0
	
	# 가로세로 2N개의 길 체크
	for x in range(N):
		R = [data[x][y] for y in range(N)]
		result += check(N, L, R)
		
		C = [data[y][x] for y in range(N)]
		result += check(N, L, C)
	
	return result

if __name__ == "__main__":
	N, L = map(int, input().split())
	data = [[*map(int, input().split())] for _ in range(N)]
	
	print(solve(N, L, data))
	
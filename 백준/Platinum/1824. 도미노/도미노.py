import sys
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
NOT_MATCHED = -1

def analyse(N, M, W):
	wall = [[[False] * 4 for _ in range(M)] for _ in range(N)]
	
	for a, b in W:
		arow, acol = a // M, a % M
		brow, bcol = b // M, b % M
		
		for x in range(4):
			if (arow + dr[x], acol + dc[x]) == (brow, bcol):
				wall[arow][acol][x] = wall[brow][bcol][(x + 2) % 4] = True
	
	return wall

def solve(N, M, W):
	wall = analyse(N, M, W)
	
	# 1. (row, col)의 합이 홀수, 짝수인 그룹으로 나눈다.
	A, B = [], []
	index = [[-1] * M for _ in range(N)]
	
	for row in range(N):
		for col in range(M):
			group = A if (row + col) % 2 else B
			
			index[row][col] = len(group)
			group.append((row, col))
	
	# 2. 도미노의 제약 조건에 따라 그래프를 모델링한다.
	LA, LB = len(A), len(B)
	graph = [[] for _ in range(LA)]
	
	for row in range(N):
		for col in range(M):
			if (row + col) % 2 == 0:
				continue
			
			for x in range(4):
				nrow, ncol = row + dr[x], col + dc[x]
				
				if not (0 <= nrow < N and 0 <= ncol < M):
					continue
				
				if wall[row][col][x]:
					continue
				
				graph[index[row][col]].append(index[nrow][ncol])
	
	# 3. 최대 매칭을 구한다.
	GA, GB = [NOT_MATCHED] * LA, [NOT_MATCHED] * LB
	
	def match(check, a):
		check[a] = True
		
		for b in graph[a]:
			if GB[b] == NOT_MATCHED or (not check[GB[b]] and match(check, GB[b])):
				GA[a], GB[b] = b, a
				return True
		
		return False
	
	result = []
	
	for a in range(LA):
		if GA[a] != NOT_MATCHED:
			continue
		
		match([False] * LA, a)
	
	# 4. 모든 도미노를 출력한다.
	for a in range(LA):
		arow, acol = A[a]
		brow, bcol = B[GA[a]]
		
		P, Q = arow * M + acol + 1, brow * M + bcol + 1
		
		if P > Q:
			P, Q = Q, P
			
		result.append((P, Q))
	
	result.sort()
	return result

if __name__ == '__main__':
	N, M = map(int, input().split())
	L = int(input())
	
	W = []
	
	for _ in range(L):
		a, b = map(int, input().split())
		W.append((a - 1, b - 1))

	result = solve(N, M, W)
	
	for p, q in result:
		print(p, q)
	
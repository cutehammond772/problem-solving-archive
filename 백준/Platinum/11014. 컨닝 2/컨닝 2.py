import sys
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()
NOT_MATCHED = -1

# 홀수 열의 학생들만 고려하기 때문에
# 짝수 열의 학생들도 모두 고려하기 위해서는 아랫 방향도 확인해야 한다.
dr, dc = [-1, 0, 1, 1, 0, -1], [1, 1, 1, -1, -1, -1]

def bipartite_matching(LA, LB, conflict):
	GA, GB = [NOT_MATCHED] * LA, [NOT_MATCHED] * LB
	result = 0
	
	def match(visited, a):
		visited[a] = True
		
		for b in conflict[a]:
			if GB[b] == NOT_MATCHED or (not visited[GB[b]] and match(visited, GB[b])):
				GA[a], GB[b] = b, a
				return True
		
		return False
	
	for a in range(LA):
		if GA[a] != NOT_MATCHED:
			continue
		
		visited = [False] * LA
		result += match(visited, a)
	
	return result

def solve(N, M, matrix):
	# 홀수 열, 짝수 열 각각 두 그룹으로 나눌 수 있다.
	# 그룹 내에서는 관계가 존재하지 않으므로 이분 그래프를 형성할 수 있다.
	A, B = [], []
	
	for row in range(N):
		for col in range(M):
			if matrix[row][col] == '.':
				(A if col % 2 else B).append((row, col))
	
	LA, LB = len(A), len(B)
	conflict = [[] for _ in range(LA)]
	
	def get_candidate(a):
		row, col = A[a]
		candidate = set()
		
		for x in range(6):
			nrow, ncol = row + dr[x], col + dc[x]
			
			if not (0 <= nrow < N and 0 <= ncol < M):
				continue
			
			if matrix[nrow][ncol] == 'x':
				continue
			
			candidate.add((nrow, ncol))
		
		return candidate
	
	# 충돌 관계를 형성한다.
	for a in range(LA):
		candidate = get_candidate(a)
		
		for b in range(LB):
			if B[b] in candidate:
				conflict[a].append(b)
	
	matches = bipartite_matching(LA, LB, conflict)
	
	# 최대 독립 집합 = (정점 수) - (최소 정점 커버 = 최대 매칭)
	return (LA + LB) - matches

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		N, M = map(int, input().split())
		matrix = [input() for _ in range(N)]
		
		print(solve(N, M, matrix))
		
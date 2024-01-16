import sys
sys.setrecursionlimit(10 ** 5)

input = lambda: sys.stdin.readline().rstrip()
NOT_MATCHED = -1

# 이분 매칭
def solve(N, M, adj):
	GA, GB = [NOT_MATCHED] * (N + 1), [NOT_MATCHED] * (M + 1)
	visited = [False] * (N + 1)
	
	# 최대 매칭 수
	result = 0
	
	# A 그룹의 노드가 B 그룹의 노드와 매치가 가능한지 확인한다.
	def match(a):
		visited[a] = True
		
		for b in adj[a]:
			if GB[b] == NOT_MATCHED or (not visited[GB[b]] and match(GB[b])):
				GA[a] = b
				GB[b] = a
				
				return True
		
		return False
	
	for a in range(1, N + 1):
		if GA[a] != NOT_MATCHED:
			continue
		
		visited = [False] * (N + 1)
		result += match(a)
	
	return result
	
if __name__ == '__main__':
	N, M = map(int, input().split())
	adj = [[] for _ in range(N + 1)]
	
	for a in range(1, N + 1):
		S, *A = map(int, input().split())
		adj[a].extend(A)
	
	print(solve(N, M, adj))
	
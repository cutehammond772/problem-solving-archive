import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()
DEPTH = 20

def solve(N, R, graph, queries):
	# 1. LCA 구성
	ancestor = [[0] * DEPTH for _ in range(N + 1)]
	level = [0] * (N + 1)
	
	# 해당 노드가 트리의 루트일 때, 해당 서브트리의 노드의 개수
	nodes = [0] * (N + 1)
	
	def traverse(prev, node):
		count = 1
		ancestor[node][0] = prev
		
		for x in range(1, DEPTH):
			ancestor[node][x] = ancestor[ancestor[node][x - 1]][x - 1]
		
		for next in graph[node]:
			if prev == next:
				continue
			
			level[next] = level[node] + 1
			count += traverse(node, next)
		
		nodes[node] = count
		return count
	
	traverse(0, 1)
	
	# 2. 쿼리 수행
	result = []
	
	def lca(x, y):
		if level[x] < level[y]:
			x, y = y, x
		
		for i in range(DEPTH - 1, -1, -1):
			if level[ancestor[x][i]] <= level[y]:
				continue
			
			x = ancestor[x][i]
		
		px, x = x, ancestor[x][0]
		
		if x == y:
			return px, y, x
		
		for i in range(DEPTH - 1, -1, -1):
			nx, ny = ancestor[x][i], ancestor[y][i]
			
			if nx == ny:
				continue
			
			x, y = nx, ny
		
		# 두 노드의 LCA의 "이전 노드"와 LCA
		return x, y, ancestor[x][0]
	
	for S, U in queries:
		# 수도의 위치 옮기기
		if S == 0:
			R = U
		
		# 세금 출력하기
		if S == 1:
			# 수도와 같은 경우, 모든 노드가 대상이다.
			if R == U:
				result.append(N)
				continue
				
			px, py, A = lca(R, U)
			
			# LCA가 R 또는 다른 노드인 경우, U의 서브트리의 노드가 대상이다.
			if A != U:
				result.append(nodes[U])
			
			# LCA가 U인 경우, 수도 R은 U를 루트로 하는 서브트리 안에 존재한다.
			else:
				result.append(N - nodes[px])
	
	return result

if __name__ == '__main__':
	T = int(input())
	
	for i in range(1, T + 1):
		N, Q, R = map(int, input().split())
		graph = [[] for _ in range(N + 1)]
		queries = []
		
		for _ in range(N - 1):
			A, B = map(int, input().split())
			
			graph[A].append(B)
			graph[B].append(A)
		
		for _ in range(Q):
			S, U = map(int, input().split())
			queries.append((S, U))
		
		taxes = solve(N, R, graph, queries)
		
		print(f"Case #{i}:")
		print(*taxes, sep='\n')
		
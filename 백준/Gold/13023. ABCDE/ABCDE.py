import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, adj):
	found = False
	visited = [False] * N
	
	def traverse(node, count):
		nonlocal found
		if found:
			return
		
		if count >= 5:
			found = True
			return
		
		for next in adj[node]:
			if visited[next]:
				continue
				
			visited[next] = True
			traverse(next, count + 1)
			visited[next] = False
	
	for x in range(N):
		if found:
			break
		
		visited[x] = True
		traverse(x, 1)
		visited[x] = False
		
	if found:
		return 1
	
	return 0
	
if __name__ == '__main__':
	N, M = map(int, input().split())
	adj = [set() for _ in range(N)]
	
	for _ in range(M):
		P, Q = map(int, input().split())
		adj[P].add(Q)
		adj[Q].add(P)
		
	print(solve(N, adj))
	
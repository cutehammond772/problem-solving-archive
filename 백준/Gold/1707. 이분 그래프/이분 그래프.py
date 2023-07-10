import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(V, adj):
	memo = [-1] * (V + 1)
	result = True
	
	for node in range(1, V + 1):
		if memo[node] >= 0:
			continue
		
		stack = [(0, node)]
		memo[node] = 0
		
		while stack and result:
			group, node = stack.pop()
			
			for next in adj[node]:
				if memo[next] == group:
					result = False
					break
				
				if memo[next] == -1:
					memo[next] = 1 - group
					stack.append((1 - group, next))
					
	return "YES" if result else "NO"
	
if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		V, E = map(int, input().split())
		adj = [set() for _ in range(V + 1)]
		
		for _ in range(E):
			X, Y = map(int, input().split())
			adj[X].add(Y)
			adj[Y].add(X)
		
		print(solve(V, adj))
		
import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def analyse(graph, tree, parent, node):
	for child in graph[node]:
		if parent == child:
			continue
		
		tree[node] += analyse(graph, tree, node, child)
	
	return tree[node]

if __name__ == "__main__":
	N, R, Q = map(int, input().split())
	graph = [[] for _ in range(N + 1)]
	
	for _ in range(N - 1):
		U, V = map(int, input().split())
		
		graph[U].append(V)
		graph[V].append(U)
	
	tree = [1] * (N + 1)
	tree[R] = analyse(graph, tree, 0, R)
	
	for _ in range(Q):
		U = int(input())
		print(tree[U])

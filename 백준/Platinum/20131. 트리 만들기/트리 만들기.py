import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

# 단말 노드 중 가장 큰 것부터 붙인다.
# 비단말 노드의 서브트리가 완성되면 해당 노드 또한 단말 노드 힙에 추가한다.
def solve(N, A):
	# 트리
	graph = [[] for _ in range(N + 1)]
	
	# 비단말 노드
	count = [0] * (N + 1)
	
	for node in A:
		count[node] += 1
	
	candidate = []
	
	for node in range(1, N + 1):
		if not count[node]:
			heappush(candidate, -node)
	
	for x in range(N - 2):
		node = -heappop(candidate)
		
		if node < A[x]:
			graph[node].append(A[x])
		else:
			graph[A[x]].append(node)
		
		count[A[x]] -= 1
		
		if count[A[x]] == 0:
			heappush(candidate, -A[x])
	
	# 마지막 한 간선
	graph[-max(candidate)].append(-min(candidate))
	return graph

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	G = solve(N, A)
	
	for node in range(1, N + 1):
		G[node].sort()
		
		for next in G[node]:
			print(node, next)
	
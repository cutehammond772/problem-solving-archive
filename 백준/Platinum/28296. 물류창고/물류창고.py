import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

def find(U, x):
	if U[x] == x:
		return U[x]
	
	nodes = [x]
	
	while U[nodes[-1]] != nodes[-1]:
		nodes.append(U[nodes[-1]])
	
	for node in nodes:
		U[node] = nodes[-1]
	
	return U[x]

def solve(N, K, C, E):
	# 1. 배송 상한선을 최대화하기 위해서는, 상한선이 큰 양방향 도로부터 뽑아야 한다. (Max Spanning Tree)
	E.sort()
	
	# 각 회사에 속한 물류창고끼리의 배송 상한선들의 총합
	result = [0] * (K + 1)
	
	# 분리 집합
	U = [*range(N + 1)]
	T = [1] * (N + 1)
	G = [defaultdict(int) for _ in range(N + 1)]
	
	for node in range(1, N + 1):
		G[node][C[node]] += 1
	
	# 간선 개수
	count = 0
	
	# 2. Tree의 성질 중 하나는, 두 정점 간의 경로는 유일하다는 것이다.
	# 즉, 특정 간선을 뽑아 두 트리(정점)를 합치는 경우
	# 두 트리 내의 정점 간의 최대 배송 상한선은 뽑은 간선의 상한선이 될 수밖에 없다.
	# 왜냐하면, 상한선이 가장 큰 간선부터 뽑고 (1)
	# 해당 간선을 통해 두 정점 간의 경로가 확정되기 (2) 때문이다.
	while count < N - 1:
		W, X, Y = E.pop()
		X, Y = find(U, X), find(U, Y)
		
		# 동일한 트리 그룹 내에 존재하는 경우
		if X == Y:
			continue
			
		# Small to Large
		if T[X] <= T[Y]:
			X, Y = Y, X
			
		U[Y] = U[X]
		T[X] += T[Y]
		
		for company in G[Y]:
			result[company] += W * G[X][company] * G[Y][company]
			G[X][company] += G[Y][company]
		
		count += 1
		
	return result[1:]
	
if __name__ == "__main__":
	N, K, M = map(int, input().split())
	C = [0, *map(int, input().split())]
	
	E = []
	for _ in range(M):
		X, Y, W = map(int, input().split())
		E.append((W, X, Y))
	
	result = solve(N, K, C, E)
	print(*result, sep='\n')
	
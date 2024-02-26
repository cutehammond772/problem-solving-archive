import sys
input = lambda: sys.stdin.readline().rstrip()
BLUE, RED = 0, 1

def find(U, x):
	if U[x] == x:
		return U[x]
	
	nodes = [x]
	
	while U[nodes[-1]] != nodes[-1]:
		nodes.append(U[nodes[-1]])
	
	for node in nodes:
		U[node] = nodes[-1]
	
	return U[x]

def union(U, X, a, b):
	a, b = find(U, a), find(U, b)
	
	if X[a] < X[b]:
		a, b = b, a
	
	U[b] = U[a]
	X[a] += X[b]
	
def solve(N, E):
	# Union-Find
	U = [*range(N + 1)]
	X = [1] * (N + 1)
	
	# result (Blue: 0, Red: 1)
	edges = [0, 0]
	count = 0
	
	for C, F, T in E:
		# 스패닝 트리의 간선의 개수는 N-1개이다.
		if count >= N - 1:
			break
		
		F, T = find(U, F), find(U, T)
		
		if F == T:
			continue
		
		union(U, X, F, T)
		edges[C] += 1
		count += 1
	
	# 스패닝 트리를 만들 수 없는 경우
	if count < N - 1:
		return [-1, -1]
	
	return edges

if __name__ == '__main__':
	while (data := input()) != "0 0 0":
		N, M, K = map(int, data.split())
		E = []
		
		for _ in range(M):
			C, F, T = input().split()
			E.append((RED if C == 'R' else BLUE, int(F), int(T)))
			
		# Red First (= Min Blue Edges)
		E.sort(key=lambda x: 1 - x[0])
		min_blue = solve(N, E)[0]
		
		# Blue First (= Max Blue Edges)
		E.sort(key=lambda x: x[0])
		max_blue = solve(N, E)[0]
		
		if min_blue == -1 or max_blue == -1:
			print(0)
		else:
			print(1 if min_blue <= K <= max_blue else 0)
		
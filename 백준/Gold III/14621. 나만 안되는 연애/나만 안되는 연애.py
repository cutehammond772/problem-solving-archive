import sys
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

def union(U, x, y):
	x, y = find(U, x), find(U, y)
	
	if U[x] <= U[y]:
		U[y] = U[x]
	else:
		U[x] = U[y]

def solve(N, E):
	U = [*range(N + 1)]
	count, cost = 0, 0
	
	E.sort(reverse=True)
	
	while E and count < N - 1:
		d, u, v = E.pop()
		u, v = find(U, u), find(U, v)
		
		if u == v:
			continue
		
		count += 1
		cost += d
		
		union(U, u, v)
	
	if count < N - 1:
		return -1
	
	return cost

if __name__ == "__main__":
	N, M = map(int, input().split())
	
	# 각 대학교의 정보 (남초 / 여초)
	R = [0, *input().split()]
	
	# 후보 간선
	E = []
	
	for _ in range(M):
		U, V, D = map(int, input().split())
		
		if R[U] == R[V]:
			continue
		
		E.append((D, U, V))
	
	print(solve(N, E))
	
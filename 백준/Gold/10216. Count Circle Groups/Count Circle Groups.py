import sys
input = lambda: sys.stdin.readline().rstrip()

def dist2(xi, yi, xj, yj):
	return (xi - xj) ** 2 + (yi - yj) ** 2

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

def solve(N, A):
	result = N
	U = [*range(N)]
	
	for i in range(N - 1):
		for j in range(i + 1, N):
			xi, yi, ri = A[i]
			xj, yj, rj = A[j]
			
			if find(U, i) == find(U, j):
				continue
			
			if dist2(xi, yi, xj, yj) <= (ri + rj) ** 2:
				union(U, i, j)
				result -= 1
	
	return result

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		A = []
		
		for _ in range(N):
			x, y, r = map(int, input().split())
			A.append((x, y, r))
		
		print(solve(N, A))
	
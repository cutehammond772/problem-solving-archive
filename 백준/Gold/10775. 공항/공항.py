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
	U[x] = U[y] = min(U[x], U[y])

def solve(G, A):
	result = 0
	U = [*range(G + 1)]
	
	for x in A:
		if (x := find(U, x)) == 0:
			break
		
		union(U, x, x - 1)
		result += 1
	
	return result

if __name__ == '__main__':
	G, P = int(input()), int(input())
	A = [int(input()) for _ in range(P)]
	
	print(solve(G, A))
	
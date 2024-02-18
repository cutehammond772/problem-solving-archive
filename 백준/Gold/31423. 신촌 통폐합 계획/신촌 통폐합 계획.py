import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N = int(input())
	S = [input() for _ in range(N)]
	G = [[] for _ in range(N)]
	
	off = 0
	
	for _ in range(N - 1):
		i, j = map(int, input().split())
		
		G[i - 1].append(j - 1)
		off = i - 1
	
	queue = [off]
	result = []
	
	while queue:
		node = queue.pop()
		result.append(S[node])
		
		queue.extend(G[node][::-1])
	
	print("".join(result))
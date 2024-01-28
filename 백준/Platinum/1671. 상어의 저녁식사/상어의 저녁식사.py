import sys
input = lambda: sys.stdin.readline().rstrip()
NOT_MATCHED = -1

def check(x, y):
	return x[0] >= y[0] and x[1] >= y[1] and x[2] >= y[2]

def solve(N, S):
	# 잡아먹는 상어(A), 잡아먹히는 상어(B)
	GA, GB = [NOT_MATCHED] * (N * 2), [NOT_MATCHED] * N
	
	# 포식 관계
	relation = [[] for _ in range(N * 2)]
	
	for a in range(N):
		for b in range(N):
			# 능력치가 같은 경우, 서로가 서로를 (또는 자기 자신을) 잡아먹지 못하도록 한다.
			if S[a] == S[b] and a >= b:
				continue
				
			if check(S[a], S[b]):
				relation[2 * a - 1].append(b)
				relation[2 * a].append(b)
	
	matches = 0
	
	def match(visited, i):
		visited[i] = True
		
		for j in relation[i]:
			if GB[j] == NOT_MATCHED or (not visited[GB[j]] and match(visited, GB[j])):
				GA[i], GB[j] = j, i
				return True
		
		return False
	
	for i in range(N * 2):
		if GA[i] != NOT_MATCHED:
			continue
		
		visited = [False] * (N * 2)
		matches += match(visited, i)
	
	return N - matches

if __name__ == "__main__":
	N = int(input())
	S = []
	
	for _ in range(N):
		a, b, c = map(int, input().split())
		S.append((a, b, c))
	
	print(solve(N, S))
	
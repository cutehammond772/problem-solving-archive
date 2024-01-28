import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 4)

NOT_MATCHED = -1
BLANK = (-1, -1)

def solve(H, V, conflict):
	GH, GV = [NOT_MATCHED] * H, [NOT_MATCHED] * V
	matches = 0
	
	def match(visited, h):
		visited[h] = True
		
		for v in conflict[h]:
			if GV[v] == NOT_MATCHED or (not visited[GV[v]] and match(visited, GV[v])):
				GH[h], GV[v] = v, h
				return True
		
		return False
	
	for h in range(H):
		if GH[h] != NOT_MATCHED:
			continue
		
		visited = [False] * H
		matches += match(visited, h)
	
	# 최대 독립 집합
	return (H + V) - matches

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		H, V = map(int, input().split())
		WH = []
		
		mark = [[BLANK] * 2001 for _ in range(2001)]
		
		# 충돌하는 부분
		conflict = [[] for _ in range(H)]
		
		for h in range(H):
			x, y, w = input().split()
			
			x, y = int(x), int(y)
			WH.append(w)
			
			for k in range(len(w)):
				# (가로 단어, 단어 내 글자의 인덱스)
				mark[x + k][y] = (h, k)
		
		for v in range(V):
			x, y, w = input().split()
			x, y = int(x), int(y)
			
			for k in range(len(w)):
				if mark[x][y + k] != BLANK:
					h, i = mark[x][y + k]
					
					if WH[h][i] != w[k]:
						conflict[h].append(v)
		
		print(solve(H, V, conflict))
		
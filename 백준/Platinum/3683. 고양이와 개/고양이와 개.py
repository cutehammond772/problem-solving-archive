import sys
input = lambda: sys.stdin.readline().rstrip()
NOT_MATCHED = -1
CAT, DOG = 1 << 10, 1 << 11

def convert(x):
	node = 0
	
	if x[0] == 'C':
		node |= CAT
	
	elif x[0] == 'D':
		node |= DOG
	
	node |= int(x[1:])
	return node

# 충돌하는 관계의 최대 매칭 수를 제외하면 시청자는 최대가 된다.
def max_match(LC, LD, conflict):
	GC, GD = [NOT_MATCHED] * LC, [NOT_MATCHED] * LD
	result = 0
	
	def match(visited, c):
		visited[c] = True
		
		for d in conflict[c]:
			if GD[d] == NOT_MATCHED or (not visited[GD[d]] and match(visited, GD[d])):
				GC[c], GD[d] = d, c
				return True
		
		return False
	
	for c in range(LC):
		if GC[c] != NOT_MATCHED:
			continue
		
		visited = [False] * LC
		result += match(visited, c)
	
	return result

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		c, d, v = map(int, input().split())
		
		# 고양이 진출을 원하는 시청자, 개 진출을 원하는 시청자
		C, D = [], []
		
		for i in range(v):
			like, hate = map(convert, input().split())
			
			if like & CAT:
				C.append((like ^ CAT, hate ^ DOG))
			
			elif like & DOG:
				D.append((hate ^ CAT, like ^ DOG))
		
		LC, LD = len(C), len(D)
		
		# 서로 투표가 충돌하는 시청자
		conflict = [[] for _ in range(LC)]
		
		for x in range(LC):
			for y in range(LD):
				if C[x][0] == D[y][0] or C[x][1] == D[y][1]:
					conflict[x].append(y)
		
		# 최대 독립 집합을 구한다.
		result = max_match(LC, LD, conflict)
		print(v - result)
	
import sys, math
input = lambda: sys.stdin.readline().rstrip()

def dist(x1, y1, x2, y2):
	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solve(N, A):
	if N == 1:
		return 0.0
	
	# x좌표 -> y좌표 순으로 정렬
	A.sort()
	
	# x = k 축을 기준으로 y의 최대 최소를 저장
	# y의 양 끝에서 양 끝으로 이동하는 것 중 최대가 존재
	line, top, bottom = [], [], []
	
	for x, y in A:
		if not line or line[-1] != x:
			line.append(x)
			top.append(y)
			bottom.append(y)
			continue
		
		top[-1] = max(top[-1], y)
		bottom[-1] = min(bottom[-1], y)
	
	# 모든 점이 한 x = k 축에 존재하면 전파가 불가능하다.
	if len(line) == 1:
		return 0.0
	
	L = len(line)
	
	# [top, bottom]
	memo = [[0.0, 0.0] for _ in range(L)]
	
	for x in range(1, L):
		# 가장 위에 있는 점
		memo[x][0] = max(
			memo[x - 1][1] + dist(line[x - 1], bottom[x - 1], line[x], top[x]),
			memo[x - 1][0] + dist(line[x - 1], top[x - 1], line[x], top[x]),
		)
		
		# 가장 아래에 있는 점
		memo[x][1] = max(
			memo[x - 1][1] + dist(line[x - 1], bottom[x - 1], line[x], bottom[x]),
			memo[x - 1][0] + dist(line[x - 1], top[x - 1], line[x], bottom[x]),
		)
	
	return max(memo[L - 1])

if __name__ == "__main__":
	N = int(input())
	A = []
	
	for _ in range(N):
		x, y = map(int, input().split())
		A.append((x, y))
	
	print(solve(N, A))
	
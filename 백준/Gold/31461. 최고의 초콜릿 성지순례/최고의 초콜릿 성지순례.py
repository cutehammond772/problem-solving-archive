import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e20)

def solve(N, data, a, b, c, d):
	(a, b), (c, d) = min((a, b), (c, d)), max((a, b), (c, d))
	
	# x좌표가 같은 경우 한 쪽만 성지순례가 가능하다.
	if a == c:
		lmax = rmax = -INF
		l = r = 0
	
		for i in range(a - 1, -1, -1):
			l += sum(data[i])
			lmax = max(lmax, l, (l - data[i][0]), (l - data[i][1]))
			
		for i in range(c + 1, N):
			r += sum(data[i])
			rmax = max(rmax, r, (r - data[i][0]), (r - data[i][1]))
			
		return (data[a][b] + data[c][d]) + max(0, lmax, rmax)
	
	# 1. 왼쪽을 둘러보고 오는 경우
	lmax = max(data[a][b], l := sum(data[a]))
	
	for i in range(a - 1, -1, -1):
		l += sum(data[i])
		lmax = max(lmax, l, (l - data[i][0]), (l - data[i][1]))
	
	# 2. 오른쪽을 둘러보고 오는 경우
	rmax = max(data[c][d], r := sum(data[c]))
	
	for i in range(c + 1, N):
		r += sum(data[i])
		rmax = max(rmax, r, (r - data[i][0]), (r - data[i][1]))
	
	# 3. 두 가게 중간에 성지순례하는 경우
	mid_max = 0
	
	for i in range(a + 1, c):
		mid_max += max(data[i][0], data[i][1], sum(data[i]))
	
	return lmax + mid_max + rmax

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		matrix = [[0] * 2 for _ in range(N)]
		
		for i in range(2):
			data = [*map(int, input().split())]
			
			for j in range(N):
				matrix[j][i] = data[j]
			
		a, b, c, d = map(int, input().split())
		result = solve(N, matrix, a - 1, b - 1, c - 1, d - 1)
		
		print(result)
		
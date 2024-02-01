import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 100001

def solve(M, T, P, Q):
	LQ, RQ = Q[:P][::-1], Q[P + 1:]
	left, right = [INF] * 100001, [INF] * 100001
	left[0] = right[0] = 0
	
	# 왼쪽 이동 시
	for move in range(len(LQ)):
		people = LQ[move]
		
		for total in range(100000, people - 1, -1):
			if left[total - people] != INF:
				left[total] = min(left[total], move + 1)
	
	# 오른쪽 이동 시
	for move in range(len(RQ)):
		people = RQ[move]
		
		for total in range(100000, people - 1, -1):
			if right[total - people] != INF:
				right[total] = min(right[total], move + 1)
	
	target = M - Q[P]
	
	# 최소 이동 시간
	result = INF
	
	# 1. 한 쪽으로만 이동하는 경우
	if left[target] != INF:
		result = min(result, left[target])
	
	if right[target] != INF:
		result = min(result, right[target])
		
	# 2. 양 쪽을 누비는 경우
	for x in range(target - 1, 0, -1):
		y = target - x
		
		if left[x] != INF and right[y] != INF:
			result = min(result, left[x] * 2 + right[y], left[x] + right[y] * 2)
	
	return "YES" if result <= T else "NO"

if __name__ == "__main__":
	N, M, T = map(int, input().split())
	Q = [*map(int, input().split())]
	P = int(input())
	
	print(solve(M, T, P - 1, Q))
	
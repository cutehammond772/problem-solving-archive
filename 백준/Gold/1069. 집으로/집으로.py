import sys, math
input = lambda: sys.stdin.readline().rstrip()

def solve(X, Y, D, T):
	distance = math.sqrt(X ** 2 + Y ** 2)
	
	# T가 D 이상이면, 그냥 걸어오는 것이 더 빠르다.
	if T >= D:
		return distance
	
	jumps = distance / D
	
	# 일부 거리를 남기고 점프하는 경우
	t1 = distance + math.floor(jumps) * (T - D)
	
	# 거리 이상을 점프 후 다시 돌아오는 경우
	t2 = -distance + math.ceil(jumps) * (T + D)
	
	# 점프만으로 목적지에 도달하는 경우
	t3 = max(2, math.ceil(jumps)) * T
	
	return min(t1, t2, t3)

if __name__ == '__main__':
	X, Y, D, T = map(float, input().split())
	print(solve(X, Y, D, T))
	
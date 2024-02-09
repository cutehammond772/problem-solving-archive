import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# DP with DnC Optimization
# maxEnd[i] <= maxEnd[i + 1] 성질을 통해 두 구간으로 나눌 수 있다.
if __name__ == "__main__":
	N, D = map(int, input().split())
	T = [*map(int, input().split())]
	V = [*map(int, input().split())]
	
	result = 0
	
	# (ls, rs, le, re)
	queue = deque([(0, N - 1, 0, N - 1)])
	
	# 역추적이 필요하지 않으므로 비재귀로 풀 수 있다.
	while queue:
		ls, rs, le, re = queue.popleft()
		s = (ls + rs) >> 1
		
		# maxEnd
		max_e = (0, 0)
		
		for t in range(max(s, le), min(s + D, re) + 1):
			max_e = max(max_e, ((t - s) * T[t] + V[s], t))
		
		max_val, e = max_e
		result = max(result, max_val)
		
		if ls != s:
			queue.append((ls, s - 1, le, e))
		
		if rs != s:
			queue.append((s + 1, rs, e, re))
	
	print(result)
	
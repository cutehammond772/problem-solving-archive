import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

if __name__ == "__main__":
	N = int(input())
	mp, mf, ms, mv = map(int, input().split())
	
	A = []
	for _ in range(N):
		p, f, s, v, c = map(int, input().split())
		A.append((p, f, s, v, c))
	
	result = (INF, [])
	
	for bit in range(1, 1 << N):
		p = f = s = v = c = 0
		
		for i in range(N):
			if bit & (1 << i):
				pi, fi, si, vi, ci = A[i]
				
				p += pi
				f += fi
				s += si
				v += vi
				c += ci
		
		if (mp <= p) and (mf <= f) and (ms <= s) and (mv <= v):
			result = min(result, (c, [x + 1 for x in range(N) if bit & (1 << x)]))
	
	cost, sequence = result
	
	if cost == INF:
		print(-1)
	
	else:
		print(cost)
		print(*sequence)
		
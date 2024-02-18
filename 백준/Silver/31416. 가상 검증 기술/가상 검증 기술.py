import sys, math
input = lambda: sys.stdin.readline().rstrip()

def solve(Ta, Tb, Va, Vb):
	A, B = Ta * Va, Tb * Vb
	
	if A < B:
		return B
	
	A = 0
	
	while A + Ta <= B:
		A += Ta
		Va -= 1
	
	if Va % 2:
		return A + Ta * math.ceil(Va / 2)
	
	return B + Ta * (Va // 2)

if __name__ == "__main__":
	Q = int(input())
	
	for _ in range(Q):
		Ta, Tb, Va, Vb = map(int, input().split())
		print(solve(Ta, Tb, Va, Vb))
	
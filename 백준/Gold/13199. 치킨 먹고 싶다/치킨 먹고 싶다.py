import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(P, M, F, C):
	# 주어진 돈으로 사먹을 수 있는 치킨 수
	chicken = M // P
	
	if not chicken:
		return 0

	return ((chicken - 1) * C // (F - C)) - ((chicken * C) // F)

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		P, M, F, C = map(int, input().split())
		print(solve(P, M, F, C))

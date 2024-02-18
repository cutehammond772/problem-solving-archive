import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 998_244_353

def solve(W, H, T, V):
	result = 1
	
	for xi, yi in V:
		width = min(W, xi + T) - max(1, xi - T) + 1
		height = min(H, yi + T) - max(1, yi - T) + 1
		
		result = (result * (width * height) % MOD) % MOD
	
	return result

if __name__ == "__main__":
	W, H, K, T = map(int, input().split())
	V = []
	
	for _ in range(K):
		xi, yi = map(int, input().split())
		V.append((xi, yi))
	
	print(solve(W, H, T, V))
	
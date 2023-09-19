import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	x1, y1, z1, x2, y2, z2 = map(int, input().split())
	N = int(input())
	K = [*map(int, input().split())]

	T1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
	T2 = max(K)
	T3 = sum(K) - T2

	check = [
		(T2 + T3) >= T1,
		(T1 + T3) >= T2,
	]

	if False in check:
		print("NO")
	else:
		print("YES")

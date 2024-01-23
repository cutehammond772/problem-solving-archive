import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N, M = map(int, input().split())
	print("ChongChong" if N * M == 2 else "GomGom")

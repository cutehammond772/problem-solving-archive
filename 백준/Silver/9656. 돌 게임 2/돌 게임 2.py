import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N = int(input())
	print("CY" if N % 2 else "SK")
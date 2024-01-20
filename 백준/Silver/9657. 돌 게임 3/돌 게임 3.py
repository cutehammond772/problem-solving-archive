import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N = int(input())
	G = [0, 1, 2, 3, 2, 0, 1]
	
	print("SK" if N == 1 or G[(N - 2) % 7] else "CY")
	
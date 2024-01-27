import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N = int(input())
		
		print(0 if N % 10 else 1)
	
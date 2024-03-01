import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(X, Y, a, b):
	check = [[False] * Y for _ in range(X)]
	result = 0
	
	for row in range(X):
		for col in range(Y):
			if check[row][col]:
				continue
				
			nrow, ncol = row + a, col + b
			
			if 0 <= nrow < X and 0 <= ncol < Y:
				check[nrow][ncol] = True
			
			result += 1
	
	return result

if __name__ == '__main__':
	T = int(input())
	
	for _ in range(T):
		X, Y, a, b = map(int, input().split())
		print(solve(X, Y, a, b))
		
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N = int(input())
	Q = []

	for _ in range(N):
		_, y = map(int, input().split())
		Q.append(y)

	Q.append(0)

	result, stack = 0, []

	for height in Q:
		while stack and stack[-1] >= height:
			result += height < stack.pop()

		stack.append(height)

	print(result)

import sys
input = lambda: sys.stdin.readline().rstrip()
START, END = ord('0'), ord('9')

if __name__ == '__main__':
	S = input()
	L = len(S)

	# 괄호의 위치
	brackets = []

	# 문자열 길이 정보
	stack = [0]

	# 오프셋
	off = 0

	while off < L:
		Q = S[off]

		if START <= ord(Q) <= END:
			if (off + 1) < L and S[off + 1] == '(':
				brackets.append(int(Q))
				stack.append(0)
				off += 2

			else:
				stack[-1] += 1
				off += 1

		elif Q == ')':
			total = stack.pop() * brackets.pop()
			stack[-1] += total
			off += 1

	print(stack[0])
	
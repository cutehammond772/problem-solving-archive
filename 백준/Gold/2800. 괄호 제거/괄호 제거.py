import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(S):
	stack, brackets = [], []
	result = []

	# 괄호 찾기
	for x in range(len(S)):
		if S[x] == '(':
			stack.append(x)

		if S[x] == ')':
			brackets.append((stack.pop(), x))

	for bit in range(1, 1 << len(brackets)):
		sequence = [*S]

		for x in range(len(brackets)):
			if (1 << x) & bit:
				p, q = brackets[x]
				sequence[p] = sequence[q] = ''

		result.append(''.join(sequence))

	# ((?))인 경우, 같은 형태의 식이 두 개 이상 나올 수 있다.
	result = [*set(result)]
	result.sort()

	return result

if __name__ == "__main__":
	S = input()
	result = solve(S)

	print(*result, sep='\n')

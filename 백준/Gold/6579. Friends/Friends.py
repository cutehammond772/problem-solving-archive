import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(S):
	groups = []
	operators = []
	i = 0
	
	while i < len(S):
		# 1. 소괄호 안의 내용을 먼저 처리한다.
		if S[i] == "(":
			left, right = 1, 0
			end = i + 1
			
			while left != right:
				left += S[end] == '('
				right += S[end] == ')'
				end += 1
			
			groups.append(solve(S[(i + 1):(end - 1)]))
			i = end
		
		# 2. 중괄호의 경우 집합을 나타낸다.
		elif S[i] == '{':
			end = i
			
			while S[end] != '}':
				end += 1
			
			elements = set(S[(i + 1):end])
			
			if operators and operators[-1] == '*':
				groups.append(groups.pop() & elements)
				operators.pop()
			
			else:
				groups.append(elements)
				
			i = end + 1
		
		# 3. 연산자는 따로 추가한다.
		elif S[i] in ['*', '+', '-']:
			operators.append(S[i])
			i += 1
		
	result = groups[0]
	
	for i in range(len(operators)):
		if operators[i] == '+':
			result |= groups[i + 1]
		
		if operators[i] == '-':
			result -= groups[i + 1]
	
	return result

if __name__ == '__main__':
	while S := input():
		result = [*solve([*S])]
		result.sort()
		
		print("{", "".join(result), "}", sep="")
		
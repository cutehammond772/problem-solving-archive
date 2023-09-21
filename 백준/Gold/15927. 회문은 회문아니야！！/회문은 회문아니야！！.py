import sys
input = lambda: sys.stdin.readline().rstrip()

def checkPalindrome(S):
	x, y = 0, len(S) - 1

	while x < y:
		if S[x] != S[y]:
			return False

		x += 1
		y -= 1

	return True

def solve(S):
	# Case 1. 모든 문자가 같으면 팰린드롬이 성립하지 않는 문자열은 없다.
	if len(set(S)) == 1:
		return -1

	# Case 2. 전체 문자열이 팰린드롬이 아닌 경우 그 문자열이 최대이다.
	if not checkPalindrome(S):
		return len(S)

	# Case 3. 전체 문자열이 팰린드롬인 경우 앞 또는 뒤에 한 글자를 빼면
	# 팰린드롬이 성립되지 않는다. (모든 문자가 같은 경우 제외)
	return len(S) - 1

if __name__ == "__main__":
	S = input()
	print(solve(S))

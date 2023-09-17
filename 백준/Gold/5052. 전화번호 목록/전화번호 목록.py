import sys
input = lambda: sys.stdin.readline().rstrip()
EXIST = "."

def solve(A):
	# 길이 순으로 정렬한다.
	# 동일한 전화번호는 없으므로 같은 길이의 전화번호 끼리는 고려할 필요가 없다.
	A.sort(key=lambda s: len(s))
	trie = {}

	for number in A:
		current = trie

		for x in number:
			if x not in current:
				current[x] = {}

			current = current[x]

			if EXIST in current:
				return "NO"

		current[EXIST] = True

	return "YES"

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		N = int(input())
		A = [input() for _ in range(N)]

		print(solve(A))

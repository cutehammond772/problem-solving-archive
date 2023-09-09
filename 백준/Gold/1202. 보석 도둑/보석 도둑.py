import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

# 이 아이디어의 핵심은,
# 최대한 높은 가격의 물건부터 (=1순위) 작은 크기의 가방에 (=2순위) 먼저 들어가도록 하는 것이다.
def solve(J, B):
	result = 0

	# 현재 (무게적으로) 가방에 넣을 수 있는 보석들이다.
	candidates = []

	# 크기가 작은 가방 순으로 정렬한다.
	B.sort()

	# 보석의 경우 먼저 크기 역순으로 정렬한다. (stack.pop() 이용하기 위함)
	J.sort(key=lambda t: t[1], reverse=True)
	
	# 가능한 후보들만 먼저 선정한 뒤, 그 중 무게가 가장 큰 보석을 고르면 된다.
	for bag in B:
		while J and J[-1][1] <= bag:
			heappush(candidates, J.pop())

		if not candidates:
			continue

		V, M = heappop(candidates)
		result += -V

	return result

if __name__ == "__main__":
	N, K = map(int, input().split())
	J, B = [], []

	for _ in range(N):
		M, V = map(int, input().split())

		# 높은 가격 -> 작은 무게
		J.append((-V, M))

	for _ in range(K):
		C = int(input())
		B.append(C)

	print(solve(J, B))

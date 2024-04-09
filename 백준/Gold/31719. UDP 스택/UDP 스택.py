import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
	idx = 1
	S1, S2 = [], []

	while A:
		# 1. 순열의 가장 앞 원소를 꺼낸다.
		num = A.popleft()

		# 2. 한 스택은 무조건 열려 있으므로, 그대로 넣을 수 있으면 바로 통과시킨다.
		if idx == num:
			idx += 1
			continue

		# 3. 기존에 스택에 있는 원소들이 떨어졌을 경우 재배열이 가능한지 확인한다.
		if S1 and idx == S1[0]:
			idx = S1[-1] + 1
			S1 = []

		if S2 and idx == S2[0]:
			idx = S2[-1] + 1
			S2 = []

		# S2 -> S1, S1 -> S2를 모두 고려하기 위해 한 번 더 추가한다.
		if S1 and idx == S1[0]:
			idx = S1[-1] + 1
			S1 = []

		# 4. 특정 스택에 넣을 수 있으면 넣고, 아니면 빈 자리에 넣는다.
		if S1 and S1[-1] + 1 == num:
			S1.append(num)
			continue

		if S2 and S2[-1] + 1 == num:
			S2.append(num)
			continue

		if not S1:
			S1.append(num)
			continue

		if not S2:
			S2.append(num)
			continue

		# 5. 아무 데도 넣을 수 없으면 오름차순으로 재배열이 불가능한 경우이다.
		return "NO"

	# 6. 덩어리가 남은 경우 서로 무조건 합칠 수 있다.
	return "YES"

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		N = int(input())
		A = deque(map(int, input().split()))

		print(solve(A))

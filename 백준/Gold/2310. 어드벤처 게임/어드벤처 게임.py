import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, maze, room_info, room_cost):
	# 각 방에 들어갔을 때의 최대 소지금
	max_cost = [-1] * (N + 1)

	# (소지금, 방 위치)
	stack = [(0, 1)]

	# N번 방까지 도달 여부
	possible = False

	while stack:
		cost, node = stack.pop()

		if node == N:
			possible = True
			break

		for next in maze[node]:
			# 빈 방
			if room_info[next] == 'E':
				if max_cost[next] < cost:
					max_cost[next] = cost
					stack.append((cost, next))

			# 레프리콘
			elif room_info[next] == 'L':
				next_cost = max(cost, room_cost[next])

				if max_cost[next] < next_cost:
					max_cost[next] = next_cost
					stack.append((next_cost, next))

			# 트롤
			elif room_info[next] == 'T':
				next_cost = cost - room_cost[next]

				if next_cost >= 0 and max_cost[next] < next_cost:
					max_cost[next] = next_cost
					stack.append((next_cost, next))

	return "Yes" if possible else "No"

if __name__ == '__main__':
	while N := int(input()):
		maze = [[] for _ in range(N + 1)]

		room_info = ['E'] * (N + 1)
		room_cost = [0] * (N + 1)

		for node in range(1, N + 1):
			room, cost, *next = input().split()

			room_info[node] = room
			room_cost[node] = int(cost)

			maze[node].extend(map(int, next[:-1]))

		print(solve(N, maze, room_info, room_cost))

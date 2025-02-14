import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

mappings = {
    "B": 0,
    "L": 1,
    "D": 2,
}


def solve(N, S):
    # (count, order, left, right)
    queue = deque([(0, 0, 0, N - 1)])
    memo = [[-1] * N for _ in range(N)]
    result = 0

    while queue:
        count, order, left, right = queue.popleft()

        if left > right:
            continue

        if memo[left][right] >= 0:
            continue

        memo[left][right] = count

        if order == mappings[S[left]]:
            result = max(result, count + 1)
            queue.append((count + 1, (order + 1) % 3, left + 1, right))

        if order == mappings[S[right]]:
            result = max(result, count + 1)
            queue.append((count + 1, (order + 1) % 3, left, right - 1))

    return result


if __name__ == '__main__':
    N = int(input())
    S = input()

    result = solve(3 * N, S)
    print(result)

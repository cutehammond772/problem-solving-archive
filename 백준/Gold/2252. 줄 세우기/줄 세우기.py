import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve(N, C, G):
    nodes, result = [], []

    # 1. Extract Root Nodes
    for i in range(1, N + 1):
        if C[i] == 0:
            nodes.append(i)

    # 2. Topological Sorting
    queue = deque(nodes)

    while queue:
        node = queue.popleft()
        result.append(node)

        for next in G[node]:
            C[next] -= 1

            if C[next] == 0:
                queue.append(next)

    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    C = [0] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        C[B] += 1

    result = solve(N, C, G)
    print(*result)

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(101010)


def solve(N, G, order):
    # DFS
    index = 0

    def traverse(node):
        nonlocal index

        if index >= N - 1:
            return

        next_node = order[index + 1]

        if next_node not in G[node]:
            return

        index += 1
        traverse(next_node)

        if index < N - 1:
            traverse(node)

    traverse(1)
    return 1 if index == N - 1 else 0


if __name__ == '__main__':
    N = int(input())
    G = [set() for _ in range(N + 1)]

    for _ in range(N - 1):
        P, Q = map(int, input().split())
        G[P].add(Q)
        G[Q].add(P)

    order = [*map(int, input().split())]
    result = solve(N, G, order)

    print(result)

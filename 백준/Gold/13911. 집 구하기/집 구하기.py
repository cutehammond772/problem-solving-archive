import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e20)


def dijkstra(V, G, limit, vertices):
    dest = [INF] * (V + 1)
    heap = []

    # 모든 세권에 대해 정점 추가
    for node in vertices:
        heappush(heap, (0, node))
        dest[node] = 0

    while heap:
        dist, node = heappop(heap)

        if dest[node] < dist:
            continue

        for cost, next in G[node]:
            next_dist = dist + cost

            # 최단 거리 제한
            if next_dist >= dest[next]:
                continue

            if next_dist > limit:
                continue

            dest[next] = next_dist
            heappush(heap, (next_dist, next))

    return dest


def solve(V, G, x, y, macs, bucks):
    checker = [True] * (V + 1)

    # 일반 정점 체크
    for node in macs:
        checker[node] = False

    for node in bucks:
        checker[node] = False

    # 맥세권, 스세권 구하기
    mac_dest = dijkstra(V, G, x, macs)
    bucks_dest = dijkstra(V, G, y, bucks)

    # 최단 거리 구하기
    result = (INF, INF)

    for node in range(1, V + 1):
        if not checker[node]:
            continue

        result = min(result, (mac_dest[node] + bucks_dest[node], node))

    return result


if __name__ == '__main__':
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((w, v))
        G[v].append((w, u))

    # 맥세권
    M, x = map(int, input().split())
    macs = [*map(int, input().split())]

    # 스세권
    S, y = map(int, input().split())
    bucks = [*map(int, input().split())]

    dist, node = solve(V, G, x, y, macs, bucks)
    print(dist if dist < INF else -1)

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

if __name__ == '__main__':
    M, N, V = map(int, input().split())
    X, Y = map(int, input().split())

    matrix = [[*map(int, input().split())] for _ in range(M)]
    volcano = [[False] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    queue = deque([])

    for _ in range(V):
        Xi, Yi, Ti = map(int, input().split())

        # (x, y, t, is_person)
        queue.append((Xi - 1, Yi - 1, -Ti, False))
        volcano[Xi - 1][Yi - 1] = True

    queue.append((X - 1, Y - 1, 0, True))
    visited[X - 1][Y - 1] = True

    # Result
    result = (matrix[X - 1][Y - 1], 0)

    while queue:
        x, y, t, is_person = queue.popleft()

        if t < 0:
            queue.append((x, y, t + 1, is_person))
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < M and 0 <= ny < N):
                continue

            if is_person:
                if visited[nx][ny] or volcano[nx][ny]:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny, t + 1, True))

                result = max(result, (matrix[nx][ny], -(t + 1)))
            else:
                if visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny, t + 1, False))

    print(result[0], -result[1])

import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N, Z, M = map(int, input().split())
    obstacles = [*map(int, input().split())]

    check = [False] * (N + 1)
    result = Z - 1

    for obstacle in obstacles:
        check[obstacle] = True

    for K in range(1, Z):
        if result < K:
            break

        visited = [False] * (N + 1)
        location = 1

        while not visited[location]:
            visited[location] = True

            if check[location]:
                break

            if location == Z:
                result = K
                break

            location = location + K

            if location > N:
                location = location - N

    print(result)

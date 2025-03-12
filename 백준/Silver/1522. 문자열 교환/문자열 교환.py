import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, S):
    count = [0] * (N + 1)
    result = 1001

    for x in range(1, N + 1):
        has_a = S[x] == 'a'
        count[x] = count[x - 1] + (1 if has_a else 0)

    # 중간 구간
    for t in range(1, N - count[N] + 2):
        left, right = t, t + count[N] - 1

        result = min(result, count[N] - (count[right] - count[left - 1]))

    # 양쪽 구간
    for t in range(2, count[N] + 1):
        left, right = t, t + (N - count[N]) - 1

        result = min(result, count[right] - count[left - 1])

    return result


if __name__ == '__main__':
    S = input()
    print(solve(len(S), "_" + S))

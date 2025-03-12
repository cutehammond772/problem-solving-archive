import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    A = []

    for i in range(N):
        B = [*map(int, input().split())]
        A = [*A, *B]

        A.sort()

        if i > 0:
            A = A[N:]

    print(A[0])

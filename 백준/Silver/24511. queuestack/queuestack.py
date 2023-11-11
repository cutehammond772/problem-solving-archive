import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]
  B = [*map(int, input().split())]

  M = int(input())
  C = [*map(int, input().split())]

  # STACK의 경우 기존 값이 그대로 유지되며, QUEUE의 경우 최근 값으로 변경된다.
  # 즉, 리턴 값의 수열은 [QUEUE 역순 -> 입력값 수열][:M]이다.
  queues = [B[x] for x in range(N - 1, -1, -1) if A[x] == 0]
  print(*[*queues, *C][:M])

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
  case = 1

  while data := input():
    N, M = map(int, data.split())

    if N == M == 0:
      break

    result = 0

    adj = [[] for _ in range(N + 1)]
    discovered = [False] * (N + 1)

    for _ in range(M):
      A, B = map(int, input().split())

      adj[A].append(B)
      adj[B].append(A)

    for node in range(1, N + 1):
      if discovered[node]:
        continue

      # DFS로 사이클 여부를 확인한다.
      is_tree = True

      stack = [(0, node)]
      discovered[node] = True

      while stack:
        prev, node = stack.pop()

        for next in adj[node]:
          if prev == next:
            continue

          if discovered[next]:
            is_tree = False
            continue

          discovered[next] = True
          stack.append((node, next))

      if is_tree:
        result += 1

    if result == 0:
      print(f"Case {case}: No trees.")

    elif result == 1:
      print(f"Case {case}: There is one tree.")

    else:
      print(f"Case {case}: A forest of {result} trees.")

    case += 1

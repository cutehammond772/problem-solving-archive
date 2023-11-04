import sys
input = lambda: sys.stdin.readline().rstrip()

# G(0) = 0
# G(1) = { 0 } = 1
# G(2) = 0
# G(3) = { 0, 1 } = 2
# G(4) = { 2 } = 1
# G(5) = { 0, 1, 3 } = 3
# G(6) = { 2, 4 } = 2
# G(7) = { 0, 1, 3, 5 } = 4

# [홀수] G(2n + 1) = n + 1
# [짝수] G(2n) = max(0, n - 1)

if __name__ == "__main__":
  N = int(input())
  P = [*map(int, input().split())]

  result = 0

  for Pi in P:
    if Pi % 2:
      result ^= (Pi - 1) // 2 + 1
    else:
      result ^= max(0, Pi // 2 - 1)

  print("koosaga" if result else "cubelover")

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(X, N, Q):
  if len(Q) < N:
    return [-1]

  if N == 1:
    return [0]

  # 최대값을 최소화, 최소값을 최대화해야 한다.
  # 최대값의 최소는 최상위 숫자 1이며, 최소값의 최대는 하위 숫자를 전부 더한 것이다.
  result = [X - sum(Q[:(offset := len(Q) - (N - 1))])]

  for k in range(offset + 1, len(Q) + 1):
    result.append(X - sum(Q[:k]))

  return result

if __name__ == '__main__':
  X, N = map(int, input().split())
  Q = [1 << i for i in range(60) if X & (1 << i)]
  
  print(*solve(X, N, Q))

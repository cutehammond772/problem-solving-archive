import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 9 + 1

def solve(A, B, C, D):
  # 2를 곱한 횟수
  P = 0
  
  # 결과
  result = INF
  
  # 목표 숫자를 넘는 순간 성립 X
  while A <= C and B <= D:
    # 차이가 동일한 경우, +1 연산만 따지기
    if C - A == D - B:
      Q, R = 0, C - A

      for x in range(P, -1, -1):
        Q += R // (2 ** x)
        R %= (2 ** x)
      
      result = min(result, P + Q)

    # 차이가 같아질 때까지 2 곱하기
    A *= 2
    B *= 2
    P += 1

  return -1 if result == INF else result

if __name__ == '__main__':
  A, B, C, D = map(int, input().split())
  print(solve(A, B, C, D))

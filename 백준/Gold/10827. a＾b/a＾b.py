import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  A, B = input().split()
  A1, A2 = A.split('.')

  # 소수점을 무시하고 제곱한 값을 구한다.
  P, Q = int(A1 + A2), int(B)
  result = str(P ** Q)
  diff = len(A2) * Q - len(result)

  # 소수점의 자리보다 수의 자리수가 작거나 같으면, 앞에 0을 채운다.
  if diff >= 0:
    print("0." + ("0" * (len(A2) * Q - len(result))) + result)

  # 소수점의 자리에 맞춰 숫자를 .으로 끊는다.
  else:
    print(result[:-diff] + "." + result[-diff:])

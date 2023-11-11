import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  # 약수의 개수가 짝수이면 창문은 닫혀 있다.
  # 즉, 특정한 수를 구성하는 소인수의 구성에서 각 소인수의 차수는 무조건 짝수여야 한다.
  # 이때, 모든 차수는 2의 배수이므로 2로 묶으면 특정한 수의 제곱으로 나타낼 수 있다.
  # 따라서, "제곱수"만이 약수의 개수가 홀수가 된다.
  print(int(N ** 0.5))

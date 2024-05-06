import sys, math
input = lambda: sys.stdin.readline().rstrip()

# N (1 <= N <= 20)에 대해 전처리
case = [0] * 21

# f(n) = n! - nC1 * f(n - 1) - nC2 * f(n - 2) - ... - nCn-2 * f(2) - 1
# -> n개 중 n - 1개를 뽑는 경우 나머지 하나는 무조건 동일한 자리로 배정되므로 한 가지만 존재한다.
for n in range(2, 21):
  case[n] += math.factorial(n) - 1
  
  for i in range(1, n - 1):
    case[n] -= math.comb(n, i) * case[n - i]

if __name__ == "__main__":
  T = int(input())
  
  for _ in range(T):
    N = int(input())
    print(case[N])
  
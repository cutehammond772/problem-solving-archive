import sys
input = lambda: sys.stdin.readline().rstrip()

def question(p, q):
  print(f"? {p} {q}")
  sys.stdout.flush()

  return int(input())

# 아이디어 : (1, 1->N), (N->1, N)와 같이 질문하여 중복이 존재하는 원소의 위치를 알아낼 수 있다.
if __name__ == '__main__':
  N = int(input())

  # 중복 체크
  check = [False] * N
  f_count, b_count = 0, 0

  # Forward
  for i in range(1, N + 1):
    response = question(1, i)

    if f_count >= response:
      check[i - 1] = True

    f_count = response

  # Backward
  for i in range(N, 0, -1):
    response = question(i, N)

    if b_count >= response:
      check[i - 1] = True

    b_count = response

  result = [x + 1 for x in range(N) if not check[x]]
  print(f"! {len(result)}", *result)

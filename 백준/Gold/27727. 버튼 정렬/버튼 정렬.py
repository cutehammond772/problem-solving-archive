import sys
input = lambda: sys.stdin.readline().rstrip()

# (필요한 버튼 횟수, 비내림차순 충족 여부)
def check(N, A, t):
  # 버튼 횟수
  need = 0

  for i in range(N - 1):
    if max(A[i], t) > max(A[i + 1], t):
      return -1, False

  for i in range(N):
    need += max(A[i], t) - A[i]

  return need, True

def create_sequence(N, A, x):
  sequence = []
  current, count = 0, 0

  for i in range(N):
    element = max(x, A[i])

    if current == 0:
      current, count = element, 1

    elif current == element:
      count += 1

    else:
      sequence.append((current, count))
      current, count = element, 1

  sequence.append((current, count))
  return sequence

def solve(N, A, K):
  # 1. 비내림차순을 충족하는 최소 버튼 횟수 및 수열을 구한다.
  x, y = 1, 10 ** 9
  min_need = 10 ** 18

  while x <= y:
    mid = (x + y) >> 1
    need, valid = check(N, A, mid)

    if valid:
      y = mid - 1
      min_need = need

    else:
      x = mid + 1

  # 최소 버튼 횟수보다 K가 작으면 정렬 횟수는 0이다.
  if min_need > K:
    return 0

  # 2. 해당 수열에 대해 남은 버튼 횟수가 존재하면 가능한 경우를 따진다.
  K -= min_need

  # 처음부터 정렬된 상태이면 정렬 횟수로 간주하지 않는다.
  result = 1 if min_need else 0
  sequence = create_sequence(N, A, y + 1)

  for i in range(len(sequence) - 1):
    element, count = sequence[i]
    next_element, next_count = sequence[i + 1]

    if K // count < next_element - element:
      break

    result += next_element - element
    K -= count * (next_element - element)

    sequence[i + 1] = (next_element, count + next_count)

  # 3. 모든 수열을 평평하게 채워도 남으면, 원소의 개수만큼 버튼을 눌러 정렬을 한 번 수행할 수 있다.
  if sequence[-1][1] == N:
    result += K // N

  return result

if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]
  K = int(input())

  print(solve(N, A, K))

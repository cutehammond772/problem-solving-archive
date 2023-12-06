import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(E):
  result = []
  idx = 0

  while idx < len(E):
    if E[idx] == '(':
      offset, count = idx, 1

      while count:
        idx += 1

        if E[idx] == '(': count += 1
        elif E[idx] == ')': count -= 1

      sub_result = solve(E[(offset + 1):idx])

      if len(sub_result) > 1 and offset > 0 and E[offset - 1] == '-':
          result.append(f'({sub_result})')

      else:
        result.append(sub_result)

    else:
      result.append(E[idx])

    idx += 1

  return ''.join(result)

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    E = input().replace(' ', '')
    print(solve(E))

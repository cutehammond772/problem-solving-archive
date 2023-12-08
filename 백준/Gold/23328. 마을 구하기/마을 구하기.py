import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, bomb, S):
  shield = bomb.lower()
  bombs, shields = 0, 0
  result = []

  for i in range(N):
    if S[i] == bomb:
      bombs += 1

    elif S[i] == shield:
      shields += 1

    else:
      result.append(S[i])

  # Case 1. 쉴드가 1개 이하
  if shields <= 1:
    bomb_string = bomb * bombs
    shield_string = shield * shields

    result.sort()
    result = "".join(result)

    return min(
      (bomb_string + shield_string) + result,
      result + (shield_string + bomb_string)
    )

  # Case 2. 쉴드가 2개 이상
  else:
    candidate = []

    # aAAAAaaaa...
    c1 = shield + (bomb * bombs) + (shield * (shields - 1))
    r1 = result[:] + [c1]

    r1.sort()
    candidate.append("".join(r1))

    # AAAaBCDEF...
    c2 = (bomb * bombs) + shield
    r2 = result[:] + ([shield] * (shields - 1))

    r2.sort()
    candidate.append(c2 + "".join(r2))

    return min(candidate)

if __name__ == "__main__":
  N, B = input().split()
  S = [*input()]

  print(solve(int(N), B, S))

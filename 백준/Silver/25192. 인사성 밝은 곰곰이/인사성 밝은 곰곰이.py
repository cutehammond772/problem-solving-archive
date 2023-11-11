import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  result = 0
  users = set()

  for _ in range(N):
    user = input()

    if user == 'ENTER':
      result += len(users)
      users.clear()

    else:
      users.add(user)

  result += len(users)
  print(result)

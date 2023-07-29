import sys
input = lambda: sys.stdin.readline().rstrip()
END = chr(ord('Z') + 1)

if __name__ == '__main__':
  N = int(input())
  words = [input() + END for _ in range(N)]

  while words:
    words.sort()
    ch = words[0][0]

    if ch != END:
      print(ch, end='')
      words[0] = words[0][1:]
    else:
      words = words[1:]

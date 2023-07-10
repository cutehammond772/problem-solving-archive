import sys
input = lambda: sys.stdin.readline().rstrip()
END = '0'

def make_trie(N):
  trie = {}
  
  for _ in range(N):
    S = input()
    L = len(S)
  
    current = trie
  
    for x in range(L):
      if S[x] not in current:
        current[S[x]] = {}
    
      current = current[S[x]]
  
    # 단어의 마지막에 별도로 표시
    current[END] = 0
  
  return trie

def solve(S, colors, nicknames):
  L = len(S)
  color_pt = colors
  
  for x in range(L):
    if S[x] not in color_pt:
      break
    
    if END in color_pt[S[x]] and S[(x + 1):] in nicknames:
      return "Yes"
      
    color_pt = color_pt[S[x]]
    
  return "No"

if __name__ == '__main__':
  C, N = map(int, input().split())
  
  colors = make_trie(C)
  nicknames = {input() for _ in range(N)}
  
  Q = int(input())
  for _ in range(Q):
    S = input()
    print(solve(S, colors, nicknames))

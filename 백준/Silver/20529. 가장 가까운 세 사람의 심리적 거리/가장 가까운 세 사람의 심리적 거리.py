import sys
input = lambda: sys.stdin.readline().rstrip()

MBTIs = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
MBTIindexes = { MBTIs[x]: x for x in range(16) }

def dist(x, y):
  result = 0
  
  for idx in range(4):
    if MBTIs[x][idx] != MBTIs[y][idx]:
      result += 1
      
  return result

def convert(mbti):
  return MBTIindexes[mbti]

def preprocess(A):
  types = set()
  counts = [0] * 16

  for mbti in A:
    types.add(mbti)
    counts[mbti] += 1

  return types, counts

def solve(types, counts, D):
  result = 49
  used, total = [0] * 16, [0] * 3
  
  for x in range(16):
    if counts[x] - used[x] == 0:
      continue

    # 첫번째 mbti
    used[x] += 1
    total[0] = x
    
    for y in range(16):
      if counts[y] - used[y] == 0:
        continue

      # 두번째 mbti
      used[y] += 1
      total[1] = y
      
      for z in range(16):
        if counts[z] - used[z] == 0:
          continue

        # 세번째 mbti
        used[z] += 1
        total[2] = z

        result = min(result, D[total[0]][total[1]] + D[total[1]][total[2]] + D[total[0]][total[2]])
        
        used[z] -= 1
      used[y] -= 1
    used[x] -= 1
    
  return result

if __name__ == '__main__':
  T = int(input())
  D = [[dist(x, y) for x in range(16)] for y in range(16)]
  
  for _ in range(T):
    N = int(input())
    A = [*map(convert, input().split())]

    print(solve(*preprocess(A), D))
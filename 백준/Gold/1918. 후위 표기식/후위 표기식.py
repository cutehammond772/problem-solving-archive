def solve(expression):
  # 괄호를 처리하기 위한 배열
  first_par = -1
  par_count = 0
  
  # 괄호가 모두 풀린 레벨 1 토큰
  lv1_tokens = []

  # 곱셈, 뺄셈이 처리된 레벨 2 토큰
  lv2_offset = 0
  lv2_tokens = []

  # 덧셈, 뺄셈이 처리된 레벨 3 토큰
  lv3_offset = 0
  lv3_tokens = []
  
  # 괄호 안의 식을 먼저 처리
  for idx in range(len(expression)):
    token = expression[idx]
    
    if token == '(':
      if par_count == 0:
        first_par = idx
        
      par_count += 1
    elif token == ')':
      par_count -= 1
      
      if par_count == 0:
        lv1_tokens.append(solve(expression[first_par + 1 : idx]))
    elif par_count == 0:
      lv1_tokens.append(token)
  
  # 일반 식 처리: 곱셈과 나눗셈을 먼저 처리
  while lv2_offset < len(lv1_tokens):
    token = lv1_tokens[lv2_offset]
    
    if not (token == '*' or token == '/'):
      lv2_tokens.append(token)
      lv2_offset += 1
      continue

    previous = lv2_tokens.pop()
    lv2_tokens.append(previous + lv1_tokens[lv2_offset + 1] + token)

    # 뒷부분의 미지수는 넘어감
    lv2_offset += 2
  
  # 일반 식 처리: 덧셈과 뺄셈을 먼저 처리
  while lv3_offset < len(lv2_tokens):
    token = lv2_tokens[lv3_offset]
    
    if not (token == '+' or token == '-'):
      lv3_tokens.append(token)
      lv3_offset += 1
      continue

    previous = lv3_tokens.pop()
    lv3_tokens.append(previous + lv2_tokens[lv3_offset + 1] + token)

    # 앞의 미지수 부분은 넘어감
    lv3_offset += 2
  
  return ''.join(lv3_tokens)

if __name__ == '__main__':
  expression = input()
  print(solve(expression))
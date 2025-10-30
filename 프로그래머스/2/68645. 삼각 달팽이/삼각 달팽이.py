def solution(n):
    arr = [[0] * (x + 1) for x in range(n)]
    num_off, row_off, col_off = 1, 0, 0
    
    # 각 삼각형의 숫자 대입
    for x in range(n, 0, -3):
        # 왼쪽 테두리
        for i in range(x):
            arr[row_off + i][col_off] = num_off + i
        
        # 아래쪽 테두리
        for i in range(x):
            arr[row_off + (x - 1)][col_off + i] = num_off + (x - 1) + i
        
        # 오른쪽 테두리
        for i in range(x - 1):
            arr[row_off + (x - 1) - i][col_off + (x - 1) - i] = num_off + 2 * (x - 1) + i
        
        # 안쪽 삼각형으로 오프셋 설정
        num_off += (3 * x) - 3
        row_off += 2
        col_off += 1
    
    # 평탄화
    answer = []
    
    for row in arr:
        answer.extend(row)
    
    return answer
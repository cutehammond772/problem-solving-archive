function solution(board) {
    // 상수
    const [O, X] = [0, 1];
    const N = board.length;
    
    // 규칙 1: O는 X보다 최대 1개 더 많아야 한다.
    const count = [0, 0];
    
    // 규칙 2: O와 X에서 빙고가 동시에 나올 수 없다.
    const bingo = [0, 0];
    
    // 1. OX 개수 체크
    for (let row = 0; row < N; row++) {
        for (let col = 0; col < N; col++) {
            if (board[row][col] === 'O') {
                count[O]++;
            } else if (board[row][col] === 'X') {
                count[X]++;
            }
        }
    }
    
    if (count[O] < count[X] || count[O] - count[X] > 1) {
        return 0;
    }
    
    // 2. 빙고 개수 체크
    
    // 2-1. 행 빙고
    for (let row = 0; row < N; row++) {
        const countOnRow = [0, 0];
        
        for (let col = 0; col < N; col++) {
            if (board[row][col] === 'O') {
                countOnRow[O]++;
            } else if (board[row][col] === 'X') {
                countOnRow[X]++;
            }
        }
        
        if (countOnRow[O] === N) {
            bingo[O]++;
        } else if (countOnRow[X] === N) {
            bingo[X]++;
        }
    }
    
    // 2-2. 열 빙고
    for (let col = 0; col < N; col++) {
        const countOnColumn = [0, 0];
        
        for (let row = 0; row < N; row++) {
            if (board[row][col] === 'O') {
                countOnColumn[O]++;
            } else if (board[row][col] === 'X') {
                countOnColumn[X]++;
            }
        }
        
        if (countOnColumn[O] === N) {
            bingo[O]++;
        } else if (countOnColumn[X] === N) {
            bingo[X]++;
        }
    }
    
    // 2-3-1. 정방향 대각선 빙고
    {
        const countOnDiagonal = [0, 0];
        
        for (let x = 0; x < N; x++) {
            if (board[x][x] === 'O') {
                countOnDiagonal[O]++;
            } else if (board[x][x] === 'X') {
                countOnDiagonal[X]++;
            }
        }
        
        if (countOnDiagonal[O] === N) {
            bingo[O]++;
        } else if (countOnDiagonal[X] === N) {
            bingo[X]++;
        }
    }
    
    // 2-3-2. 역방향 대각선 빙고
    {
        const countOnDiagonal = [0, 0];
        
        for (let x = 0; x < N; x++) {
            if (board[(N - 1) - x][x] === 'O') {
                countOnDiagonal[O]++;
            } else if (board[(N - 1) - x][x] === 'X') {
                countOnDiagonal[X]++;
            }
        }
        
        if (countOnDiagonal[O] === N) {
            bingo[O]++;
        } else if (countOnDiagonal[X] === N) {
            bingo[X]++;
        }
    }
    
    if (bingo[O] > 0 && bingo[X] > 0) {
        return 0;
    }
    
    // 3. 빙고 상태에서 속행하는 경우
    
    // 3-1. 선공(O)이 승리한 이후에 속행
    if (bingo[O] > 0 && count[O] === count[X]) {
        return 0;
    }
    
    // 3-2. 후공(X)이 승리한 이후에 속행
    if (bingo[X] > 0 && count[O] > count[X]) {
        return 0;
    }
    
    return 1;
}
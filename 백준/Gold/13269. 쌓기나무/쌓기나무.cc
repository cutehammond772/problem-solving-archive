#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;

// 나무 블록의 존재 여부
int exist[500][500];

// 행, 열 각 라인의 나무 블록의 최대 높이
int row_height[500], col_height[500];

// 나무 모양의 충족 여부
bool row_check[500], col_check[500];

// 최종 결과
int result[500][500];

int main() {
    FAST_IO; int N, M;
    cin >> N >> M;

    for (int row = 0; row < N; row++) {
        for (int col = 0; col < M; col++) {
            cin >> exist[row][col];
        }
    }

    for (int col = 0; col < M; col++) {
        cin >> col_height[col];
    }

    for (int row = 0; row < N; row++) {
        cin >> row_height[(N - 1) - row];
    }

    /**
     * result[row][col] = (각 라인의 최대 중 작은 쪽)
     * 이어야 나무 블록이 최대가 된다.
     * 단, 이후 각 라인의 최대 값을 다시 체크해 주어야 한다.
     */
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < M; col++) {
            if (!exist[row][col]) {
                result[row][col] = 0;
                continue;
            }

            int rh = row_height[row], ch = col_height[col];
            int height = result[row][col] = min(rh, ch);

            if (rh == height) row_check[row] = true;
            if (ch == height) col_check[col] = true;
        }
    }

    for (int row = 0; row < N; row++) {
        if (!row_check[row]) {
            cout << -1 << "\n";
            return 0;
        }
    }

    for (int col = 0; col < M; col++) {
        if (!col_check[col]) {
            cout << -1 << "\n";
            return 0;
        }
    }

    for (int row = 0; row < N; row++) {
        for (int col = 0; col < M; col++) {
            cout << result[row][col] << " ";
        }
        cout << "\n";
    }
}

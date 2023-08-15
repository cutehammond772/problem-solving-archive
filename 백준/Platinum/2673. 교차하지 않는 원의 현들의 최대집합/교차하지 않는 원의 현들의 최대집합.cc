#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
int memo[101][101], chord[101][101];

int main() {
    FAST_IO;
    int N, a, b;

    cin >> N;
    memset(memo, 0, sizeof memo);
    memset(chord, 0, sizeof chord);

    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        chord[a][b] = chord[b][a] = 1;
    }
    
    // 분할 정복 DP ('행렬 곱셈 순서'와 유사)
    for (int j = 1; j <= 100; j++) {
        for (int i = j; i > 0; i--) {
            for (int k = i; k < j; k++) {
                memo[i][j] = max(memo[i][j], memo[i][k] + memo[k][j] + chord[i][j]);
            }
        }
    }

    cout << memo[1][100] << "\n";
    return 0;
}

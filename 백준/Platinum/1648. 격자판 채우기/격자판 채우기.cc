#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
constexpr int MOD = 9901;

vector<int> combs;
int memo[14][1 << 14];

// 2x1 도미노를 놓는 경우의 수를 미리 계산
void init(int N, int offset, int current) {
    if (offset >= N) {
        combs.push_back(current);
        return;
    }

    for (int i = offset; i < N - 1; i++) {
        init(N, i + 2, current | (3 << i));
    }

    combs.push_back(current);
}

int main() {
    FAST_IO;
    int N, M; cin >> N >> M;
    init(N, 0, 0);

    memset(memo, 0, sizeof memo);

    // 첫번째 열의 경우의 수
    for (auto& mask : combs)
        memo[0][mask] = 1;

    // 비트필드 DP
    for (int x = 1; x < M; x++) {
        for (int k = 0; k < 1 << N; k++) {
            if (memo[x - 1][k]) {
                int rev = k ^ ((1 << N) - 1);

                for (auto& mask : combs) {
                    if ((rev | mask) == rev + mask) {
                        memo[x][rev | mask] = (memo[x][rev | mask] + memo[x - 1][k]) % MOD;
                    }
                }
            }
        }
    }

    // 모두 채워진 경우의 수를 출력
    cout << memo[M - 1][(1 << N) - 1] << "\n";
    return 0;
}

#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define MOD 1000000007

using namespace std;
using ll = long long;

int N, M;
ll memo[301][1 << 17];

ll traverse(int off, int bit) {
    if (off > N * M) return 0;
    if (off == N * M) return 1;

    if (memo[off][bit] != -1)
        return memo[off][bit];

    auto& result = memo[off][bit];
    result = 0;

    // 1. 블록을 놓지 않는 경우
    result = (result + traverse(off + 1, bit >> 1)) % MOD;

    // 2. 블록을 한 칸 놓을 때, 윗행에 연속된 두 개의 블록이 설치된 경우
    // 한 칸만 놓고 한 칸은 건너뛴다.
    if ((off + 1) % M != 0 and (bit & 3) == 3) {
        result = (result + traverse(off + 2, (bit | (1 << M)) >> 2)) % MOD;
    } else {
        result = (result + traverse(off + 1, (bit | (1 << M)) >> 1)) % MOD;
    }

    return result;
}

int main() {
    FAST_IO;
    memset(memo, -1, sizeof memo);
    
    cin >> N >> M;
    if (N < M) swap(N, M);

    cout << traverse(0, 0) << "\n";
    return 0;
}

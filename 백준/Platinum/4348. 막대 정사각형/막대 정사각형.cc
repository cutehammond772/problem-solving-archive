#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define UNDEFINED 0
#define POSSIBLE 3
#define IMPOSSIBLE 1

using namespace std;

int N, total, S[20];
int L, memo[1 << 20];

int traverse(int bit, int remainder) {
    // 이미 이전 탐색에서 결정난 경우
    if (memo[bit] != UNDEFINED)
        return memo[bit];

    int result = IMPOSSIBLE;

    for (int next = 0; next < N; next++) {
        if (bit & (1 << next))
            continue;

        int size = S[next];

        if (remainder + size > L)
            continue;

        result |= traverse(bit | 1 << next, (remainder + size) % L);
    }

    return memo[bit] = result;
}

bool solve() {
    // 길이가 정확히 네 동강이 나지 않으면 정사각형을 만들 수 없다.
    if (total % 4 > 0)
        return false;

    // 정사각형의 한 변의 길이이다.
    L = total / 4;

    // memo[bitset] = (지금까지 해당 막대를 사용했을 때, 남은 막대들로 할 수 있는 가능성)
    memset(memo, UNDEFINED, sizeof memo);

    // 모두 다 채울 수 있다면 가능한 것이다.
    memo[(1 << N) - 1] = POSSIBLE;

    // 맨 처음부터 탐색을 수행한다.
    traverse(0, 0);

    // 한 경우라도 가능한 경우가 생기면 true이다.
    return memo[0] == POSSIBLE;
}

int main() {
    FAST_IO;
    int T; cin >> T;

    while (T--) {
        cin >> N;
        total = 0;

        for (int i = 0; i < N; i++) {
            cin >> S[i];
            total += S[i];
        };

        cout << (solve() ? "yes" : "no") << "\n";
    }

    return 0;
}

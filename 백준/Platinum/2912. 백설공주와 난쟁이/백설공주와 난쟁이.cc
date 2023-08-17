#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;

int N, Q, M, C;

struct query {
    int index, x, y;

    query(int index, int x, int y): index(index), x(x), y(y) {}

    bool operator<(const query& a) const {
        if (x / Q != a.x / Q) return x / Q < a.x / Q;
        return y < a.y;
    }
};

int seq[300001], result[10000], counts[10001];
vector<query> queries;

inline void add(int x) { counts[x]++; }
inline void sub(int x) { counts[x]--; }

inline int color(int K) {
    // C > K/2는 2C > K와 같다.
    for (int x = 1; x <= C; x++)
        if (2 * counts[x] > K) return x;

    return 0;
}

int main() {
    FAST_IO;

    memset(seq, 0, sizeof seq);
    memset(result, 0, sizeof result);
    memset(counts, 0, sizeof counts);

    cin >> N >> C;
    Q = (int) sqrt(N);

    for (int i = 1; i <= N; i++) cin >> seq[i];

    int l, r; cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> l >> r;
        queries.emplace_back(i, l, r);
    }

    sort(queries.begin(), queries.end());

    // 첫번째 쿼리
    auto [f, p, q] = queries[0];
    for (int i = p; i <= q; i++) add(seq[i]);
    result[f] = color(q - p + 1);

    // 나머지 쿼리
    for (int i = 1; i < M; i++) {
        auto [index, np, nq] = queries[i];

        while (p < np) sub(seq[p++]);
        while (np < p) add(seq[--p]);
        while (nq < q) sub(seq[q--]);
        while (q < nq) add(seq[++q]);

        result[index] = color(nq - np + 1);
    }

    for (int i = 0; i < M; i++) {
        if (!result[i]) cout << "no" << "\n";
        else cout << "yes " << result[i] << "\n";
    }

    return 0;
}

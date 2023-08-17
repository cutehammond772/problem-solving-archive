#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define MAX 100001

using namespace std;
using ll = long long;

ll N, Q, M, K;

struct query {
    int index, x, y;

    query(int index, int x, int y): index(index), x(x), y(y) {}

    bool operator<(const query& a) const {
        if (x / Q != a.x / Q) return x / Q < a.x / Q;
        return y < a.y;
    }
};

struct FenwickTree {
    ll tree[MAX];

    void init() { memset(tree, 0, sizeof tree); }

    void update(ll x, ll t) {
        while (0 < x && x < MAX) {
            tree[x] += t; x += x & -x;
        }
    }

    ll query(ll x) {
        ll result = 0;
        if (x >= MAX) x = 100000;

        while (x > 0) {
            result += tree[x]; x -= x & -x;
        }

        return result;
    }

} fenwick;

ll a[MAX], result[100000], accumulation = 0;
vector<query> queries;

inline void add(ll x) {
    accumulation += fenwick.query(x + K) - fenwick.query((x - K) - 1);
    fenwick.update(x, 1);
}

inline void sub(ll x) {
    fenwick.update(x, -1);
    accumulation -= fenwick.query(x + K) - fenwick.query((x - K) - 1);
}

int main() {
    FAST_IO; fenwick.init();

    memset(a, 0, sizeof a);
    memset(result, 0, sizeof result);

    cin >> N >> K;
    Q = (int) sqrt(N);

    for (int i = 1; i <= N; i++) cin >> a[i];

    int l, r; cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> l >> r;
        queries.emplace_back(i, l, r);
    }

    sort(queries.begin(), queries.end());

    // 첫번째 쿼리
    auto [f, p, q] = queries[0];
    for (int i = p; i <= q; i++) add(a[i]);
    result[f] = accumulation;

    // 나머지 쿼리
    for (int i = 1; i < M; i++) {
        auto [index, np, nq] = queries[i];

        while (p < np) sub(a[p++]);
        while (np < p) add(a[--p]);
        while (nq < q) sub(a[q--]);
        while (q < nq) add(a[++q]);

        result[index] = accumulation;
    }

    for (int i = 0; i < M; i++)
        cout << result[i] << "\n";

    return 0;
}

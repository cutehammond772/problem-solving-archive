#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;
int N, M, K;

struct query {
    int idx, x, y;

    query(int idx, int x, int y): idx(idx), x(x), y(y) {}

    // Mo's
    bool operator<(const query& t) const {
        if (x / K != t.x / K) return x / K < t.x / K;
        return y < t.y;
    }
};

vector<int> seq;
vector<query> queries;
ll result[100000];

// count of nums, count of counts
ll counts[1000001];
ll total = 0;

inline void add(ll x) {
    counts[x]++;
    total += x * (counts[x] * counts[x] - (counts[x] - 1) * (counts[x] - 1));
}

inline void sub(ll x) {
    counts[x]--;
    total += x * (counts[x] * counts[x] - (counts[x] + 1) * (counts[x] + 1));
}

int main() {
    FAST_IO; int a, i, j;

    cin >> N >> M;
    K = (int) sqrt(N);

    memset(result, 0, sizeof result);
    memset(counts, 0, sizeof counts);

    for (int x = 0; x < N; x++) {
        cin >> a;
        seq.push_back(a);
    }

    for (int x = 0; x < M; x++) {
        cin >> i >> j;
        queries.emplace_back(x, i - 1, j - 1);
    }

    sort(queries.begin(), queries.end());
    auto [f, p, q] = queries[0];

    for (int x = p; x <= q; x++) add(seq[x]);
    result[f] = total;

    for (int x = 1; x < M; x++) {
        auto [idx, np, nq] = queries[x];

        while (p < np) sub(seq[p++]);
        while (np < p) add(seq[--p]);
        while (nq < q) sub(seq[q--]);
        while (q < nq) add(seq[++q]);

        result[idx] = total;
    }

    for(int x = 0; x < M; x++) {
        cout << result[x] << "\n";
    }

    return 0;
}

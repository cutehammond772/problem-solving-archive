#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

int N, Q, sqrtN;

struct query {
    int order, x, y;

    query(const int& order, const int& x, const int& y):
            order(order), x(x), y(y) {}

    bool operator<(const query& q) const {
        if (x / sqrtN != q.x / sqrtN)
            return x / sqrtN < q.x / sqrtN;

        return y < q.y;
    }
};

struct FenwickTree {
    ll tree[200001], counts[200001];

    void update(ll i, ll x) {
        while (i <= 200000) {
            tree[i] += x;
            counts[i] += (x > 0 ? 1 : -1);

            i += i & -i;
        }
    }

    pair<ll, ll> query(ll i) {
        ll result = 0, count = 0;

        while (i > 0) {
            result += tree[i];
            count += counts[i];

            i -= i & -i;
        }

        return { result, count };
    }

} fenwick;

vector<query> queries;
ll arr[200001], result[100000];

ll current = 0;

void init() {
    memset(arr, 0, sizeof arr);
    memset(result, 0, sizeof result);

    memset(fenwick.tree, 0, sizeof fenwick.tree);
    memset(fenwick.counts, 0, sizeof fenwick.counts);
}

inline void add(ll x) {
    auto [sum_total, total_count] = fenwick.query(200000);
    auto [sum_left, left_count] = fenwick.query(x);

    current += (sum_total - sum_left) - x * (total_count - left_count); // x 초과
    current += (x * left_count) - sum_left; // x 이하

    fenwick.update(x, x);
}

inline void remove(ll x) {
    fenwick.update(x, -x);

    auto [sum_total, total_count] = fenwick.query(200000);
    auto [sum_left, left_count] = fenwick.query(x);

    current -= (sum_total - sum_left) - x * (total_count - left_count); // x 초과
    current -= (x * left_count) - sum_left; // x 이하
}

int main() {
    FAST_IO; init();

    // 1. Input
    cin >> N >> Q;
    sqrtN = (int) sqrt(N);

    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < Q; i++) {
        int x, y;
        cin >> x >> y;

        queries.emplace_back(i, x, y);
    }

    // 2. Solve
    std::sort(queries.begin(), queries.end());
    int left = -1, right = -1;

    for (auto& [order, x, y] : queries) {
        // 첫 번째 쿼리
        if (left < 0 && right < 0) {
            left = x; right = y;

            for (int i = left; i <= right; i++) add(arr[i]);

            result[order] = current;
            continue;
        }

        while (x < left) add(arr[--left]);
        while (right < y) add(arr[++right]);
        while (left < x) remove(arr[left++]);
        while (y < right) remove(arr[right--]);

        result[order] = current;
    }

    for (int i = 0; i < Q; i++)
        cout << result[i] << "\n";

    return 0;
}

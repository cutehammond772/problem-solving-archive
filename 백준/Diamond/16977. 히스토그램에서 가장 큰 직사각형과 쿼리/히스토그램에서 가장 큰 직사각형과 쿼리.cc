#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;
using mx = tuple<ll, ll, ll, ll>;

ll N, Q;

vector<tuple<ll, ll, ll>> queries;
vector<pair<ll, ll>> height;

struct segtree {
    mx tree[404040];

    segtree() {
        init(1, 1, 100000);
    }

    void init(ll node, ll left, ll right) {
        tree[node] = { 1, 0, 0, 0 };
        if (left == right) return;

        ll mid = (left + right) >> 1;

        init(node * 2, left, mid);
        init(node * 2 + 1, mid + 1, right);
    }

    void mark(ll node, ll left, ll right, ll idx) {
        if (idx < left || right < idx)
            return;

        if (left == right) {
            if (left == idx) {
                tree[node] = { 1, 1, 1, 1 };
            }

            return;
        }

        ll mid = (left + right) >> 1;

        mark(node * 2, left, mid, idx);
        mark(node * 2 + 1, mid + 1, right, idx);

        auto& [l0, l1, l2, l3] = tree[node * 2];
        auto& [r0, r1, r2, r3] = tree[node * 2 + 1];

        ll v0 = l0 + r0;
        ll v1 = max({ l1, r1, l2, r3, l3 + r2 });
        ll v2 = l0 == l2 ? l2 + r2 : l2;
        ll v3 = r0 == r3 ? l3 + r3 : r3;

        tree[node] = { v0, v1, v2, v3 };
    }

    mx query(ll node, ll left, ll right, ll l, ll r) {
        if (r < left || right < l)
            return { 0, 0, 0, 0 };

        if (l <= left && right <= r)
            return tree[node];

        ll mid = (left + right) >> 1;

        auto [l0, l1, l2, l3] = query(node * 2, left, mid, l, r);
        auto [r0, r1, r2, r3] = query(node * 2 + 1, mid + 1, right, l, r);

        ll v0 = l0 + r0;
        ll v1 = max({ l1, r1, l2, r3, l3 + r2 });
        ll v2 = l0 == l2 ? l2 + r2 : l2;
        ll v3 = r0 == r3 ? l3 + r3 : r3;

        return { v0, v1, v2, v3 };
    }
};

int main() {
    FAST_IO;

    // 1. Input
    cin >> N;
    for (ll i = 1; i <= N; i++) {
        ll h; cin >> h;
        height.emplace_back(h, i);
    }

    cin >> Q;
    for (ll i = 0; i < Q; i++) {
        ll l, r, w; cin >> l >> r >> w;
        queries.emplace_back(l, r, w);
    }

    std::sort(height.begin(), height.end(), greater<>());

    // 2. Solution
    vector<ll> result(Q, 0), left(Q, 0), right(Q, (ll) 1e9 + 1);

    while (true) {
        map<ll, vector<ll>, greater<>> pbs;
        ll count = 0;

        for (ll i = 0; i < Q; i++) {
            if (left[i] == right[i])
                continue;

            pbs[(left[i] + right[i]) >> 1].push_back(i);
            count++;
        }

        if (count == 0) break;

        ll idx = 0;
        segtree tree;

        for (auto& [mid, vec] : pbs) {
            while (idx < N && height[idx].first >= mid) {
                tree.mark(1, 1, 100000, height[idx++].second);
            }

            for (auto& i : vec) {
                auto& [l, r, w] = queries[i];
                auto [v0, v1, v2, v3] = tree.query(1, 1, 100000, l, r);

                if (max({ v1, v2, v3 }) >= w) {
                    result[i] = mid;
                    left[i] = mid + 1;
                } else {
                    right[i] = mid;
                }
            }
        }
    }

    for (auto x : result)
        cout << x << "\n";

    return 0;
}

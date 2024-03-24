#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct Gold {
    ll x, y, w;

    bool operator<(const Gold& g) const {
        if (y == g.y) return x < g.x;
        return y < g.y;
    }
};

struct Node {
    ll all = 0, lmax = 0, rmax = 0, tmax = 0;
};

struct SegTree {
    Node tree[12000];

    void update(ll node, ll left, ll right, ll x, ll w) {
        if (!((left <= x) && (x <= right)))
            return;

        if (left == right) {
            tree[node].tmax = tree[node].lmax = tree[node].rmax = (tree[node].all += w);
            return;
        }

        ll mid = (left + right) >> 1;

        update(node * 2, left, mid, x, w);
        update(node * 2 + 1, mid + 1, right, x, w);

        Node &l = tree[node * 2], &r = tree[node * 2 + 1];

        tree[node].all = l.all + r.all;
        tree[node].lmax = max(l.lmax, l.all + r.lmax);
        tree[node].rmax = max(r.rmax, r.all + l.rmax);
        tree[node].tmax = max({ l.tmax, r.tmax, l.rmax + r.lmax });
    }
};

int N;

vector<Gold> gold;
vector<ll> xs, ys;

int main() {
    FAST_IO;

    // 1. Input
    cin >> N;

    for (int i = 0; i < N; i++) {
        ll x, y, w; cin >> x >> y >> w;
        gold.push_back({ x, y, w });
        xs.push_back(x); ys.push_back(y);
    }

    // 2. Compression
    std::sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());

    std::sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());

    for (auto& [x, y, w] : gold) {
        x = lower_bound(xs.begin(), xs.end(), x) - xs.begin();
        y = lower_bound(ys.begin(), ys.end(), y) - ys.begin();
    }

    // 3. Query
    ll result = 0;

    std::sort(gold.begin(), gold.end());

    for (int i = 0; i < N; i++) {
        if (i > 0 && gold[i - 1].y == gold[i].y)
            continue;

        SegTree tree;

        for (int j = i; j < N; j++) {
            tree.update(1, 0, N - 1, gold[j].x, gold[j].w);

            // y가 바뀔 때
            if (j == N - 1 || gold[j].y != gold[j + 1].y) {
                result = max(result, tree.tree[1].tmax);
            }
        }
    }

    cout << result;

    return 0;
}

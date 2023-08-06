#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

// 입력 데이터
int arr[100000], diff[100000];

// GCD 값만을 관리하는 세그먼트 트리이다.
struct GCDSegmentTree {
    ll tree[400000];

    void init(int node, int left, int right) {
        if (left == right) {
            tree[node] = diff[left];
            return;
        }

        int mid = (left + right) / 2;
        init(node * 2, left, mid);
        init(node * 2 + 1, mid + 1, right);

        tree[node] = gcd(tree[node * 2], tree[node * 2 + 1]);
    }

    ll query(int x, int y, int node, int left, int right) {
        if (y < left || right < x)
            return 0;

        if (x <= left && right <= y)
            return tree[node];

        int mid = (left + right) / 2;
        return gcd(query(x, y, node * 2, left, mid), query(x, y, node * 2 + 1, mid + 1, right));
    }

    void update(int x, ll t, int node, int left, int right) {
        if (!(left <= x && x <= right))
            return;

        if (left == right) {
            tree[node] = t;
            return;
        }

        int mid = (left + right) / 2;
        update(x, t, node * 2, left, mid);
        update(x, t, node * 2 + 1, mid + 1, right);

        tree[node] = gcd(tree[node * 2], tree[node * 2 + 1]);
    }
} rangeGCD;

// 수열의 원소를 관리하는 레이지 세그먼트 트리이다.
struct RangeSegmentTree {
    ll tree[400000], lazy[400000];

    void init(int node, int left, int right) {
        if (left == right) {
            tree[node] = arr[left];
            return;
        }

        int mid = (left + right) / 2;
        init(node * 2, left, mid);
        init(node * 2 + 1, mid + 1, right);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    void propagate(int node, int left, int right) {
        if (!lazy[node]) return;

        tree[node] += (right - left + 1) * lazy[node];

        if (left != right) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }

        lazy[node] = 0;
    }

    void update(int x, int y, ll t, int node, int left, int right) {
        propagate(node, left, right);

        if (y < left || right < x)
            return;

        if (x <= left && right <= y) {
            tree[node] += (right - left + 1) * t;

            if (left != right) {
                lazy[node * 2] += t;
                lazy[node * 2 + 1] += t;
            }
            return;
        }

        int mid = (left + right) / 2;
        update(x, y, t, node * 2, left, mid);
        update(x, y, t, node * 2 + 1, mid + 1, right);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    ll query(int x, int node, int left, int right) {
        propagate(node, left, right);

        if (!(left <= x && x <= right))
            return 0;

        if (left == right)
            return tree[node];

        int mid = (left + right) / 2;

        if (x <= mid)
            return query(x, node * 2, left, mid);
        else
            return query(x, node * 2 + 1, mid + 1, right);
    }
} range;

int main() {
    FAST_IO;
    int N, Q, t, a, b;

    memset(range.tree, 0, sizeof range.tree);
    memset(rangeGCD.tree, 0, sizeof rangeGCD.tree);
    memset(range.lazy, 0, sizeof range.lazy);

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        diff[i] = (i > 0) ? abs(arr[i] - arr[i - 1]) : arr[i];
    }

    range.init(1, 0, N - 1);
    rangeGCD.init(1, 0, N - 1);

    cin >> Q;
    while (Q--) {
        cin >> t >> a >> b;

        if (t == 0) {
            // gcd(a + k, b - a, c - b, ...)
            ll an = range.query(a - 1, 1, 0, N - 1);
            ll bn = rangeGCD.query(a, b - 1, 1, 0, N - 1);
            cout << gcd(an, bn) << "\n";
        }
        else {
            // 수열의 구간 업데이트
            range.update(a - 1, b - 1, t, 1, 0, N - 1);

            // GCD 값 업데이트
            ll ak = range.query(a - 1, 1, 0, N - 1);
            rangeGCD.update(a - 1, abs(ak), 1, 0, N - 1);

            ll bk = range.query(b, 1, 0, N - 1) - range.query(b - 1, 1, 0, N - 1);
            rangeGCD.update(b, abs(bk), 1, 0, N - 1);
        }
    }

    return 0;
}

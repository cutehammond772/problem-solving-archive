#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct RangeSegmentTree {
    ll tree[400000], lazy[400000][2], arr[100000];

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

    // [start, skip]
    void propagate(int node, int left, int right) {
        if (!lazy[node][0]) return;

        ll start = lazy[node][0], skip = lazy[node][1];
        int mid = (left + right) / 2;

        tree[node] += (right - left + 1) * (2 * start + skip * (right - left)) / 2;

        if (left != right) {
            lazy[node * 2][0] += start;
            lazy[node * 2 + 1][0] += start + skip * (mid - left + 1);

            lazy[node * 2][1] += skip;
            lazy[node * 2 + 1][1] += skip;
        }

        lazy[node][0] = lazy[node][1] = 0;
    }

    void update(int x, int y, int node, int left, int right) {
        propagate(node, left, right);

        if (right < x || y < left)
            return;

        int mid = (left + right) / 2;
        int k = left - x + 1;

        if (x <= left && right <= y) {
            tree[node] += (right - left + 1) * (2 * k + (right - left)) / 2;

            if (left != right) {
                lazy[node * 2][0] += k;
                lazy[node * 2 + 1][0] += k + (mid - left + 1);

                lazy[node * 2][1] += 1;
                lazy[node * 2 + 1][1] += 1;
            }

            return;
        }

        update(x, y, node * 2, left, mid);
        update(x, y, node * 2 + 1, mid + 1, right);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    ll query(int x, int node, int left, int right) {
        propagate(node, left, right);

        if (!(left <= x && x <= right))
            return 0;

        if (left == right)
            return tree[node];

        int mid = (left + right) / 2;
        return query(x, node * 2, left, mid) + query(x, node * 2 + 1, mid + 1, right);
    }
} range;

int main() {
    FAST_IO;
    int N, Q, C, X, L, R;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> range.arr[i];
    }

    range.init(1, 0, N - 1);

    cin >> Q;
    while (Q--) {
        cin >> C;

        if (C == 1) {
            cin >> L >> R;
            range.update(L - 1, R - 1, 1, 0, N - 1);
        }

        if (C == 2) {
            cin >> X;
            cout << range.query(X - 1, 1, 0, N - 1) << "\n";
        }
    }

    return 0;
}

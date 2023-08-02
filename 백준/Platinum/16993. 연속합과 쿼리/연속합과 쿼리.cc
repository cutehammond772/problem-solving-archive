#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr)
#define MIN 100000001

using namespace std;
using ll = long long;

struct Node {
    ll leftMax, rightMax, rangeMax, total;
};

ll A[100001];
Node tree[400001];
Node INF = { -MIN, -MIN, -MIN, -MIN };

void init(int node, int left, int right) {
    if (left == right) {
        // [좌측 포함 최대, 우측 포함 최대, 구간 내 최대, 전체 구간 (부분합)]
        tree[node] = { A[left], A[left], A[left], A[left] };
        return;
    }

    int mid = (left + right) / 2;
    init(node * 2, left, mid);
    init(node * 2 + 1, mid + 1, right);

    auto ln = tree[node * 2];
    auto rn = tree[node * 2 + 1];

    tree[node].leftMax = max(ln.leftMax, ln.total + rn.leftMax);
    tree[node].rightMax = max(rn.rightMax, ln.rightMax + rn.total);
    tree[node].rangeMax = max({ ln.rangeMax, rn.rangeMax, ln.rightMax + rn.leftMax });
    tree[node].total = ln.total + rn.total;
}

Node query(int x, int y, int node, int left, int right) {
    if (y < left || right < x)
        return INF;

    if (x <= left && right <= y)
        return tree[node];

    int mid = (left + right) / 2;
    auto ln = query(x, y, node * 2, left, mid);
    auto rn = query(x, y, node * 2 + 1, mid + 1, right);

    return {
        max(ln.leftMax, ln.total + rn.leftMax),
        max(rn.rightMax, ln.rightMax + rn.total),
        max({ ln.rangeMax, rn.rangeMax, ln.rightMax + rn.leftMax }),
        ln.total + rn.total
    };
}

int main() {
    FAST_IO;
    int N, M, i, j;

    cin >> N;
    for (int x = 0; x < N; x++) {
        cin >> A[x];
    }

    init(1, 0, N - 1);

    cin >> M;
    while (M--) {
        cin >> i >> j;
        cout << query(i - 1, j - 1, 1, 0, N - 1).rangeMax << "\n";
    }

    return 0;
}
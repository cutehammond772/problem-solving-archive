#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr)

using namespace std;

struct wall {
    int hmin, hmax;
};

const wall DEFAULT = {-1, 100001};
wall tree[8000000], lazy[8000000];

inline void apply(wall& node, wall& apply) {
    if (node.hmin >= apply.hmax) {
        node.hmin = node.hmax = apply.hmax;
    } else if (node.hmax <= apply.hmin) {
        node.hmin = node.hmax = apply.hmin;
    } else {
        node.hmin = max(node.hmin, apply.hmin);
        node.hmax = min(node.hmax, apply.hmax);
    }
}

void propagate(int node, int left, int right) {
    apply(tree[node], lazy[node]);

    if (left != right) {
        apply(lazy[node * 2], lazy[node]);
        apply(lazy[node * 2 + 1], lazy[node]);
    }

    // 기본값으로 초기화
    lazy[node] = DEFAULT;
}

void update(int op, int x, int y, int height, int node, int left, int right) {
    propagate(node, left, right);

    if (right < x || y < left)
        return;

    if (x <= left && right <= y) {
        wall dispatch = DEFAULT;

        if (op == 1) {
            dispatch.hmin = height;
        } else if (op == 2) {
            dispatch.hmax = height;
        }

        apply(tree[node], dispatch);

        if (left != height) {
            apply(lazy[node * 2], dispatch);
            apply(lazy[node * 2 + 1], dispatch);
        }

        return;
    }

    int mid = (left + right) / 2;
    update(op, x, y, height, node * 2, left, mid);
    update(op, x, y, height, node * 2 + 1, mid + 1, right);

    wall& ln = tree[node * 2], rn = tree[node * 2 + 1];
    tree[node].hmin = min(ln.hmin, rn.hmin);
    tree[node].hmax = max(ln.hmax, rn.hmax);
}

// 특정 위치의 벽의 높이를 반환한다.
int query(int x, int node, int left, int right) {
    propagate(node, left, right);

    if (left == right)
        return tree[node].hmax;

    int mid = (left + right) / 2;

    if (x <= mid)
        return query(x, node * 2, left, mid);
    else
        return query(x, node * 2 + 1, mid + 1, right);
}

int main() {
    FAST_IO;

    for (auto &node : lazy) {
        node = DEFAULT;
    }

    int N, K, op, left, right, height;
    cin >> N >> K;

    while (K--) {
        cin >> op >> left >> right >> height;
        update(op, left, right, height, 1, 0, N - 1);
    }

    for (int i = 0; i < N; i++) {
        cout << query(i, 1, 0, N - 1) << "\n";
    }

    return 0;
}

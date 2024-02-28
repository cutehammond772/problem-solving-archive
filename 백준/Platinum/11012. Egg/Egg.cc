#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define MAX 100002

using namespace std;
using ll = long long;

struct Node {
    Node *left, *right;
    ll value;

    Node(ll value = 0): left(nullptr), right(nullptr), value(value) {}
    Node(Node* prev): left(prev->left), right(prev->right), value(prev->value) {}
};

struct PST {
    Node *root[MAX];

    void init(Node *node, int left, int right) {
        if (left == right) {
            return;
        }

        int mid = (left + right) >> 1;

        node->left = new Node();
        node->right = new Node();

        init(node->left, left, mid);
        init(node->right, mid + 1, right);
    }

    void insert(Node* node, int left, int right, int y, ll value) {
        if (y < left || right < y) return;

        if (left == right) {
            node->value += value;
            return;
        }

        int mid = (left + right) >> 1;

        if (y <= mid) {
            node->left = new Node(node->left);
            insert(node->left, left, mid, y, value);
        } else {
            node->right = new Node(node->right);
            insert(node->right, mid + 1, right, y, value);
        }

        node->value = node->left->value + node->right->value;
    }

    ll query(Node* node, int left, int right, int y1, int y2) {
        if (y2 < left || right < y1) return 0;
        if (y1 <= left && right <= y2) return node->value;

        int mid = (left + right) >> 1;

        return query(node->left, left, mid, y1, y2) + query(node->right, mid + 1, right, y1, y2);
    }
};

int main() {
    FAST_IO;
    int T; cin >> T;

    while (T--) {
        // 퍼시스턴트 세그먼트 트리
        PST tree;
        ll result = 0;

        tree.root[0] = new Node();
        tree.init(tree.root[0], 0, 100000);

        int N, M; cin >> N >> M;
        vector<int> ys[MAX];

        while (N--) {
            int x, y; cin >> x >> y;
            ys[x + 1].push_back(y);
        }

        // 누적 합
        for (int x = 1; x < MAX; x++) {
            tree.root[x] = new Node(tree.root[x - 1]);

            for (int& y : ys[x])
                tree.insert(tree.root[x], 0, 100000, y, 1);
        }

        while (M--) {
            int x1, x2, y1, y2; cin >> x1 >> x2 >> y1 >> y2;
            result += tree.query(tree.root[x2 + 1], 0, 100000, y1, y2) - tree.query(tree.root[x1], 0, 100000, y1, y2);
        }

        cout << result << "\n";
    }

    return 0;
}

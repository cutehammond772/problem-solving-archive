#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define INF (1<<30)

using namespace std;
using ll = long long;

struct Trie {
    Trie *node[2] = { nullptr, nullptr };
    int index = 0;

    explicit Trie(int index): index(index) {}
};

int N, A;
Trie* root = new Trie(30);

ll minimum(Trie* left, Trie* right) {
    ll result = INF;
    bool diff = true;

    // 1. 두 자리의 부호가 같은 경우
    for (int bit = 0; bit <= 1; bit++) {
        if (left->node[bit] && right->node[bit]) {
            diff = false;
            result = min(result, minimum(left->node[bit], right->node[bit]));
        }
    }

    if (!diff) return result;

    // 2. 두 자리의 부호가 다른 경우
    for (int bit = 0; bit <= 1; bit++) {
        if (left->node[bit] && right->node[1 - bit]) {
            result = min(result, (1 << ((left->index) - 1)) | minimum(left->node[bit], right->node[1 - bit]));
        }
    }

    return (result != INF) ? result : 0;
}

ll traverse(Trie *node, ll common) {
    if (!node->node[0] && !node->node[1])
        return 0;

    int addition = 1 << ((node->index) - 1);

    if (!node->node[0])
        return traverse(node->node[1], common | addition);

    if (!node->node[1])
        return traverse(node->node[0], common);

    // 1. 두 컴포넌트에 대해 MST 비용 구하기
    ll zero = traverse(node->node[0], common);
    ll one = traverse(node->node[1], common | addition);

    // 2. 두 컴포넌트 간 가장 작은 간선의 비용 구하기
    ll cost = addition | minimum(node->node[0], node->node[1]);

    return (zero + one) + cost;
}

int main() {
    FAST_IO;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> A;

        Trie *node = root;

        for (int x = 29; x >= 0; x--) {
            int bit = (A & (1 << x)) >> x;
            if (!node->node[bit]) node->node[bit] = new Trie(x);

            node = node->node[bit];
        }
    }

    cout << traverse(root, 0) << "\n";
    return 0;
}

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct Trie {
    Trie *zero = nullptr, *one = nullptr;
    int index = 0;

    Trie(int index): index(index) {}
};

int N, A;

Trie* root = new Trie(30);

ll minimum(Trie* left, Trie* right) {
    ll result = 1 << 30;
    bool diff = true;

    // 두 자리의 부호가 같은 경우
    if (left->zero && right->zero) {
        diff = false;
        result = min(result, minimum(left->zero, right->zero));
    }

    if (left->one && right->one) {
        diff = false;
        result = min(result, minimum(left->one, right->one));
    }

    if (!diff)
        return result;

    if (left->zero && right->one) {
        result = min(result, (1 << ((left->index) - 1)) | minimum(left->zero, right->one));
    }

    if (left->one && right->zero) {
        result = min(result, (1 << ((left->index) - 1)) | minimum(left->one, right->zero));
    }

    if (result == 1 << 30)
        return 0;

    return result;
}

ll traverse(Trie *node, ll common) {
    if (!node->zero && !node->one)
        return 0;

    int addition = 1 << ((node->index) - 1);

    if (!node->zero)
        return traverse(node->one, common | addition);

    if (!node->one)
        return traverse(node->zero, common);

    // 1. 두 컴포넌트에 대해 계산
    ll zero = traverse(node->zero, common);
    ll one = traverse(node->one, common | addition);

    // 2. 두 컴포넌트 간 가장 작은 간선의 비용 구하기
    ll cost = addition | minimum(node->zero, node->one);

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

            if (bit == 0) {
                if (!node->zero) { node->zero = new Trie(x); }
                node = node->zero;
            }

            if (bit == 1) {
                if (!(node->one)) node->one = new Trie(x);
                node = node->one;
            }
        }
    }

    cout << traverse(root, 0) << "\n";
    return 0;
}

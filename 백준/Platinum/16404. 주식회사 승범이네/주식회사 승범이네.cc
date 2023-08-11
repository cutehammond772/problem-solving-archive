#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct RangeSegmentTree {
    ll tree[400000], lazy[400000];

    void propagate(int node, int left, int right) {
        if (!lazy[node]) return;

        tree[node] += lazy[node] * (right - left + 1);

        if (left != right) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }

        lazy[node] = 0;
    }

    void update(int x, int y, int k, int node, int left, int right) {
        propagate(node, left, right);

        if (right < x || y < left)
            return;

        if (x <= left && right <= y) {
            tree[node] += k * (right - left + 1);

            if (left != right) {
                lazy[node * 2] += k;
                lazy[node * 2 + 1] += k;
            }

            return;
        }

        int mid = (left + right) / 2;
        update(x, y, k, node * 2, left, mid);
        update(x, y, k, node * 2 + 1, mid + 1, right);

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

struct EulerTour {
    vector<int> graph[100000];
    int nodeID = 0, range[100000][2];

    void init(int node) {
        range[node][0] = nodeID++;

        for (auto next : graph[node])
            init(next);

        range[node][1] = nodeID - 1;
    }
} tour;

int main() {
    FAST_IO;

    int N, M, root, command, idx, w;
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        cin >> root;

        if (i == 0) continue;
        tour.graph[root - 1].push_back(i);
    }

    // 오일러 경로 테크닉을 통해 노드 번호 정하기
    tour.init(0);

    while (M--) {
        cin >> command >> idx;
        auto& [x, y] = tour.range[idx - 1];

        if (command == 1) {
            cin >> w;

            // 자신과 부사수 모두 이익을 업데이트한다.
            range.update(x, y, w, 1, 0, N - 1);
        }

        if (command == 2) {
            // x는 자신이다.
            cout << range.query(x, 1, 0, N - 1) << "\n";
        }
    }

    return 0;
}

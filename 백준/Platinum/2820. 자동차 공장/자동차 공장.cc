#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct RangeSegmentTree {
    ll arr[500000], tree[2000000], lazy[2000000];

    void propagate(int node, int left, int right) {
        if (!lazy[node]) return;

        tree[node] += (right - left + 1) * lazy[node];

        if (left != right) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }

        lazy[node] = 0;
    }

    void update(int x, int y, ll k, int node, int left, int right) {
        propagate(node, left, right);

        if (right < x || y < left)
            return;

        if (x <= left && right <= y) {
            tree[node] += (right - left + 1) * k;

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

// 오일러 경로 테크닉 (DFS 활용)
struct RangeEulerTour {
    vector<int> adj[500000];
    pair<int, int> under[500000];
    int count = 0;

    void init(int node) {
        under[node].first = count++;
        for (auto next : adj[node]) init(next);
        under[node].second = count - 1;
    }
} tour;

int main() {
    FAST_IO;
    int N, M, a, x, boss;
    char c;

    cin >> N >> M;

    // 직원 입력 받기
    for (int i = 0; i < N; i++) {
        cin >> range.arr[i];
        if (i == 0) continue;

        cin >> boss;
        tour.adj[boss - 1].push_back(i);
    }

    // 초기화
    memset(range.tree, 0, sizeof range.tree);
    memset(range.lazy, 0, sizeof range.lazy);
    tour.init(0);

    // DFS 정렬 순서에 따라 트리에 월급을 대입한다.
    for (int i = 0; i < N; i++)
        range.update(tour.under[i].first, tour.under[i].first, range.arr[i], 1, 0, N - 1);

    while (M--) {
        cin >> c;

        if (c == 'p') {
            cin >> a >> x;

            auto& r = tour.under[a - 1];
            if (r.first == r.second) continue;

            range.update(r.first + 1, r.second, x, 1, 0, N - 1);
        }

        if (c == 'u') {
            cin >> a;
            
            // 트리의 구간은 DFS 순서를 기준으로 한다는 점에 유의한다.
            cout << range.query(tour.under[a - 1].first, 1, 0, N - 1) << "\n";
        }
    }

    return 0;
}

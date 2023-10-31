#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

constexpr ll inf = 2e18;

struct Line {
    ll a, b;

    Line(ll a, ll b): a(a), b(b) {}

    // y = ax + b
    ll get(ll x) {
        return a * x + b;
    }
};

struct Node {
    int left, right;
    ll x, y;

    // 해당 구간에서 우위를 점하는 직선이다.
    Line line;

    Node(int left, int right, ll x, ll y, ll a, ll b):
        left(left), right(right), x(x), y(y), line(a, b) {}
};

// Dynamic Segment Tree
struct LiChaoTree {
    vector<Node> tree;

    void init(ll x, ll y) {
        tree.emplace_back(-1, -1, x, y, 0, -inf);
    }

    void update(int node, Line high) {
        ll x = tree[node].x, y = tree[node].y;
        ll mid = (x + y) / 2;

        // 직선의 우위를 확인하기 위한 과정
        Line low = tree[node].line;

        // "시작점"을 기준으로 두 직선을 정렬한다.
        if (low.get(x) > high.get(x)) {
            swap(low, high);
        }

        // "끝점"에서 high가 더 크면 이 직선은 high가 항상 우위이다.
        if (low.get(y) <= high.get(y)) {
            tree[node].line = high;
            return;
        }

        // "중간 지점"에서 high가 더 크면, 이 직선은 high가 우위이다.
        if (low.get(mid) < high.get(mid)) {
            tree[node].line = high;

            // 우위가 아닌 우측 구간에 대해 처리한다.
            if (tree[node].right == -1) {
                tree[node].right = (int) tree.size();
                tree.emplace_back(-1, -1, mid + 1, y, 0, -inf);
            }

            update(tree[node].right, low);
        }

        // "중간 지점"에서 low가 같거나 크면, 이 직선은 low가 우위이다.
        else {
            tree[node].line = low;

            // 우위가 아닌 좌측 구간에 대해 처리한다.
            if (tree[node].left == -1) {
                tree[node].left = (int) tree.size();
                tree.emplace_back(-1, -1, x, mid, 0, -inf);
            }

            update(tree[node].left, high);
        }
    }

    ll query(int node, ll t) {
        if (node == -1) return -inf;

        ll x = tree[node].x, y = tree[node].y;
        ll mid = (x + y) / 2;

        // 현재 구간에서 우위인 직선과 각각의 구간에서 우위인 직선을 비교한다.
        if (t <= mid) {
            return max(tree[node].line.get(t), query(tree[node].left, t));
        }

        else {
            return max(tree[node].line.get(t), query(tree[node].right, t));
        }
    }
};

int main() {
    FAST_IO;

    int Q; cin >> Q;
    LiChaoTree tree;
    tree.init(-1e12, 1e12);

    while (Q--) {
        int c; cin >> c;

        // 직선 추가
        if (c == 1) {
            ll a, b; cin >> a >> b;
            tree.update(0, { a, b });
        }

        // 해당 구간에서의 최댓값 쿼리
        if (c == 2) {
            ll x; cin >> x;
            cout << tree.query(0, x) << "\n";
        }
    }

    return 0;
}

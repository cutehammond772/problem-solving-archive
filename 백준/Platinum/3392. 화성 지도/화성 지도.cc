#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;
using num = const int&;

struct line {
    int x, y1, y2, k;

    line(num x, num y1, num y2, num k): x(x), y1(y1), y2(y2), k(k) {};

    bool operator<(const line& l) const {
        if (x == l.x) return y1 < l.y1;

        return x < l.x;
    }
};

struct SegmentTree {
    ll tree[120001]{}, counts[30001]{};

    void update(int x, int y, int k, int node, int left, int right) {
        if (right < x || y < left)
            return;

        if (left == right) {
            tree[node] = !!(counts[left] += k);
            return;
        }

        int mid = (left + right) / 2;

        update(x, y, k, node * 2, left, mid);
        update(x, y, k, node * 2 + 1, mid + 1, right);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    ll query(int x, int y, int node, int left, int right) {
        if (right < x || y < left)
            return 0;

        if (x <= left && right <= y) {
            return tree[node];
        }

        int mid = (left + right) / 2;
        return query(x, y, node * 2, left, mid) + query(x, y, node * 2 + 1, mid + 1, right);
    }

    ll total() {
        return query(0, 30000, 1, 0, 30000);
    }
};

vector<line> lines;
SegmentTree tree;

int main() {
    FAST_IO;
    int N; cin >> N;

    // 1. 지도의 정보를 입력받는다.
    for (int i = 0; i < N; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        // 선 위의 한 점을 x라 하면 [x, x + 1)의 범위를 가지도록 해야 한다.
        line start(x1, y1, y2 - 1, 1), end(x2, y1, y2 - 1, -1);
        lines.push_back(start); lines.push_back(end);
    }

    // 2. 라인을 기준으로 정렬한다.
    sort(lines.begin(), lines.end());

    // 3. 스위핑을 통해 면적을 구한다.
    ll result = 0;
    int px = 0;

    for (auto& [x, y1, y2, k] : lines) {
        if (px != x) {
            result += (x - px) * tree.total(); px = x;
        }

        // 라인의 정보에 따라 세그먼트 트리를 갱신한다.
        tree.update(y1, y2, k, 1, 0, 30000);
    }

    cout << result << "\n";
    return 0;
}

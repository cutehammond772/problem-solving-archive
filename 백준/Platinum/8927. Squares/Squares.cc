#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct pos {
    ll x, y, xi, yi;

    pos(ll x, ll y): x(x), y(y), xi(0), yi(0) {}

    bool operator<(const pos& a) const {
        ll outer = xi * a.yi - yi * a.xi;
        if (outer) return outer > 0;
        if (y != a.y) return y < a.y;

        return x < a.x;
    }

    pos operator-(const pos& a) const {
        return { x - a.x, y - a.y };
    }
};

ll ccw(const pos& a, const pos& b, const pos& c) {
    return (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x);
}

void makeConvexHull(int& N, vector<pos>& squares) {
    // 1. y좌표 -> x좌표 작은 순 정렬
    sort(squares.begin(), squares.end());

    for (int i = 1; i < N; i++) {
        auto& square = squares[i];
        square.xi = square.x - squares[0].x;
        square.yi = square.y - squares[0].y;
    }

    // 2. 기준점 기준 반시계 방향으로 정렬
    sort(squares.begin() + 1, squares.end());

    // 3. Graham Scan
    vector<pos> result;
    result.push_back(squares[0]); result.push_back(squares[1]);
    int next = 2;

    while (next < N) {
        while (result.size() >= 2) {
            if (ccw(*(result.end() - 2), *(result.end() - 1), squares[next]) > 0)
                break;

            result.pop_back();
        }

        result.push_back(squares[next++]);
    }

    squares = result;
    N = (int) result.size();
}

ll dist2(const pos& a, const pos& b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

ll rotatingCalipers(int N, vector<pos>& squares) {
    int p = 0, q = 1;
    ll result = dist2(squares[p], squares[q]);

    for (int x = 0; x < 2 * N; x++) {
        int np = (p + 1) % N, nq = (q + 1) % N;
        ll outer = ccw({0, 0}, squares[np] - squares[p], squares[q] - squares[nq]);

        if (outer > 0) p = np;
        else if (outer < 0) q = nq;
        else { p = np; q = nq; }

        result = max(result, dist2(squares[p], squares[q]));
    }

    return result;
}

ll maxDistance(int N, vector<pos>& squares) {
    makeConvexHull(N, squares);
    ll result = rotatingCalipers(N, squares);

    return result;
}

int main() {
    FAST_IO;
    int T, N, x, y, w; cin >> T;

    while (T--) {
        vector<pos> squares;
        cin >> N;

        for (int i = 0; i < N; i++) {
            cin >> x >> y >> w;

            squares.emplace_back(x, y);
            squares.emplace_back(x + w, y);
            squares.emplace_back(x, y + w);
            squares.emplace_back(x + w, y + w);
        }

        cout << maxDistance(N * 4, squares) << "\n";
    }

    return 0;
}

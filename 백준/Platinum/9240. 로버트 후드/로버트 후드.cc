#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct Pos {
    ll x, y, xi, yi;
    Pos(ll x, ll y) : x(x), y(y), xi(0), yi(0) {}
};

vector<Pos> dots;

ll ccw(const Pos& a, const Pos& b, const Pos& c) {
    return (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x);
}

ll dist2(const Pos& a, const Pos& b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

bool cmp(const Pos& a, const Pos& b) {
    ll deg = a.xi * b.yi - a.yi * b.xi;
    if (deg) return deg > 0;

    if (a.y != b.y) return a.y < b.y;
    else return a.x < b.x;
}

// 볼록 껍질 구하기
vector<int> convexHull(int N) {
    vector<int> result;

    // y좌표가 작은 순 -> x좌표가 작은 순
    stable_sort(dots.begin(), dots.end(), cmp);

    // 기준점을 기준으로 하는 위치벡터로 변환
    for (int i = 1; i < N; i++) {
        dots[i].xi = dots[i].x - dots[0].x;
        dots[i].yi = dots[i].y - dots[0].y;
    }

    // 기준점에 대해 반시계 방향으로 정렬
    stable_sort(dots.begin() + 1, dots.end(), cmp);
    result.push_back(0); result.push_back(1);

    for (int next = 2; next < N; next++) {
        while (result.size() >= 2) {
            if (ccw(dots[*(result.end() - 2)], dots[*(result.end() - 1)], dots[next]) > 0)
                break;

            result.pop_back();
        }

        result.push_back(next);
    }

    return result;
}

// 회전하는 캘리퍼스
ll rotatingCalipers(int N) {
    vector<int> i = convexHull(N);
    N = (int) i.size();

    int p = 0, q = 1;
    ll dist = dist2(dots[i[p]], dots[i[q]]);

    for (int x = 0; x < 2 * N; x++) {
        int np = (p + 1) % N, nq = (q + 1) % N;
        ll deg = ccw(
                { 0, 0 },
                { dots[i[np]].x - dots[i[p]].x, dots[i[np]].y - dots[i[p]].y },
                { dots[i[q]].x - dots[i[nq]].x, dots[i[q]].y - dots[i[nq]].y }
                );

        if (deg > 0) p = np;
        else if (deg < 0) q = nq;
        else { p = np; q = nq; }

        dist = max(dist, dist2(dots[i[p]], dots[i[q]]));
    }

    return dist;
}

int main() {
    FAST_IO; cout.precision(12);
    int N, x, y; cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        dots.emplace_back(x, y);
    }

    cout << sqrtl(rotatingCalipers(N)) << "\n";
    return 0;
}

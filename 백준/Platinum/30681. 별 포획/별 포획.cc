#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct pos {
    ll x, y, xi, yi;
    pos(ll x, ll y) : x(x), y(y), xi(0), yi(0) {}
};

vector<pos> dots;

ll ccw(const pos& a, const pos& b, const pos& c) {
    return (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x);
}

long double dist(const pos& a, const pos& b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

bool cmp(const pos& a, const pos& b) {
    ll deg = a.xi * b.yi - a.yi * b.xi;
    if (deg) return deg > 0;

    if (a.y != b.y) return a.y < b.y;
    else return a.x < b.x;
}

vector<int> convexHull(int N) {
    vector<int> result;
    stable_sort(dots.begin(), dots.end(), cmp);

    for (int i = 1; i < N; i++) {
        dots[i].xi = dots[i].x - dots[0].x;
        dots[i].yi = dots[i].y - dots[0].y;
    }

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

long double rotatingCalipers(int N) {
    vector<int> i = convexHull(N);
    N = (int) i.size();

    int p = 0, q = 1;

    if (N == 2) {
        return dist(dots[i[0]], dots[i[1]]);
    }

    long double current = 0.0;
    long double result = 1.79769e+308;

    for (int x = 0; x < 3 * N; x++) {
        int np = (p + 1) % N, nq = (q + 1) % N;

        ll deg = ccw(
                { 0, 0 },
                { dots[i[np]].x - dots[i[p]].x, dots[i[np]].y - dots[i[p]].y },
                { dots[i[q]].x - dots[i[nq]].x, dots[i[q]].y - dots[i[nq]].y }
        );

        // 1. 평행 기준점 이동
        if (deg > 0) {
            result = min(result, current);
            current -= dist(dots[i[np]], dots[i[(np + 1) % N]]);
            p = np;
        }

        // 2. 밧줄 추가
        else {
            current += dist(dots[i[q]], dots[i[nq]]);
            q = nq;
        }
    }

    return result;
}

int main() {
    FAST_IO;
    int N, x, y; cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        dots.emplace_back(x, y);
    }

    cout.precision(12);
    cout << rotatingCalipers(N) << "\n";

    return 0;
}
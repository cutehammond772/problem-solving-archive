#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct Pos {
    ll x, y, xi, yi;
    Pos(ll x, ll y) : x(x), y(y), xi(0), yi(0) {}
};
using Cities = vector<Pos>;

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
vector<int> convexHull(int N, Cities& cities) {
    vector<int> result;

    // y좌표가 작은 순 -> x좌표가 작은 순
    stable_sort(cities.begin(), cities.end(), cmp);

    // 기준점을 기준으로 하는 위치벡터로 변환
    for (int i = 1; i < N; i++) {
        cities[i].xi = cities[i].x - cities[0].x;
        cities[i].yi = cities[i].y - cities[0].y;
    }

    // 기준점에 대해 반시계 방향으로 정렬
    stable_sort(cities.begin() + 1, cities.end(), cmp);
    result.push_back(0); result.push_back(1);

    for (int next = 2; next < N; next++) {
        while (result.size() >= 2) {
            if (ccw(cities[*(result.end() - 2)], cities[*(result.end() - 1)], cities[next]) > 0)
                break;

            result.pop_back();
        }

        result.push_back(next);
    }

    return result;
}

// 회전하는 캘리퍼스
pair<int, int> rotatingCalipers(int N, Cities& cities) {
    vector<int> i = convexHull(N, cities);
    N = (int) i.size();

    int p = 0, q = 1, r1 = 0, r2 = 1;
    ll maxDist = dist2(cities[i[p]], cities[i[q]]);

    for (int x = 0; x < 2 * N; x++) {
        int np = (p + 1) % N, nq = (q + 1) % N;
        ll deg = ccw(
                { 0, 0 },
                { cities[i[np]].x - cities[i[p]].x, cities[i[np]].y - cities[i[p]].y },
                { cities[i[q]].x - cities[i[nq]].x, cities[i[q]].y - cities[i[nq]].y }
                );

        if (deg > 0) p = np;
        else if (deg < 0) q = nq;
        else { p = np; q = nq; }

        ll dist = dist2(cities[i[p]], cities[i[q]]);

        if (dist > maxDist) {
            maxDist = dist;
            r1 = p; r2 = q;
        }
    }

    return { i[r1], i[r2] };
}

int main() {
    FAST_IO;
    int T, N, x, y; cin >> T;

    while (T--) {
        cin >> N;
        Cities cities;

        for (int i = 0; i < N; i++) {
            cin >> x >> y;
            cities.emplace_back(x, y);
        }

        auto [p, q] = rotatingCalipers(N, cities);
        cout << cities[p].x << " " << cities[p].y << " " << cities[q].x << " " << cities[q].y << "\n";
    }

    return 0;
}

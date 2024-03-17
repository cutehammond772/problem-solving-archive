#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define MAX 1010101

using namespace std;
using ll = long long;

ll di[] = { -1, 0, 1, 0 }, dj[] = { 0, 1, 0, -1 };

ll N, M, T, E, Q;
ll elevation[500][500], point[500][500];

bool check[500][500];
vector<tuple<ll, ll, ll>> edges;
vector<ll> queries;

struct UnionFind {
    ll U[MAX], C[MAX], A[MAX];

    // initialization
    UnionFind() {
        for (ll i = 0; i < MAX; i++) {
            U[i] = i; C[i] = 1; A[i] = 0;
        }
    }

    ll find(ll x) {
        if (U[x] == x) return x;
        return U[x] = find(U[x]);
    }

    void merge(ll w, ll x, ll y) {
        x = find(x); y = find(y);

        if (x == y) return;
        if (C[x] < C[y]) swap(x, y);

        U[y] = U[x];
        C[x] += C[y];
        A[x] = max({ w, A[x], A[y] });
    }
};

void analyse() {
    for (ll i = 0; i < N; i++) {
        for (ll j = 0; j < M; j++) {
            check[i][j] = true;

            for (ll k = 0; k < 4; k++) {
                ll ni = i + di[k], nj = j + dj[k];

                if (!((0 <= ni && ni < N) && (0 <= nj && nj < M))) continue;
                if (check[ni][nj]) continue;

                edges.emplace_back(abs(elevation[i][j] - elevation[ni][nj]), i * M + j, ni * M + nj);
            }

            if (point[i][j] == 1) {
                queries.push_back(i * M + j);
            }
        }
    }
}

int main() {
    FAST_IO;

    // 1. Input
    cin >> N >> M >> T;

    for (ll i = 0; i < N; i++) {
        for (ll j = 0; j < M; j++) {
            cin >> elevation[i][j];
        }
    }

    for (ll i = 0; i < N; i++) {
        for (ll j = 0; j < M; j++) {
            cin >> point[i][j];
        }
    }

    // 2. Analysis
    analyse();

    E = edges.size(); Q = queries.size();
    std::sort(edges.begin(), edges.end());

    // 3. Solution
    ll answer = 0;
    vector<ll> result(Q, 0), left(Q, T - 1), right(Q, E);

    while (true) {
        UnionFind uf;
        vector<vector<ll>> pbs(E + 1);

        ll count = 0;

        for (ll i = 0; i < Q; i++) {
            if (left[i] == right[i]) continue;

            pbs[(left[i] + right[i]) >> 1].push_back(i);
            count += 1;
        }

        if (count == 0) break;

        for (ll i = 0; i < E; i++) {
            auto [w, a, b] = edges[i];

            uf.merge(w, a, b);

            for (auto j : pbs[i + 1]) {
                ll k = uf.find(queries[j]);

                if (uf.C[k] >= T) {
                    result[j] = uf.A[k]; right[j] = i + 1;
                } else {
                    left[j] = i + 2;
                }
            }
        }
    }

    for (auto x : result) answer += x;
    cout << answer << "\n";

    return 0;
}

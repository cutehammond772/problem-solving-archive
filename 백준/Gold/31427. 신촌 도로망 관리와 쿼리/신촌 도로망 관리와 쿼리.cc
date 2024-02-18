#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

struct TreeInfo {
    int init;
    int e[5];
};

int N, M, Q;
ll costs[5];

struct Edge {
    int z, u, v;

    bool operator<(const Edge& e) const {
        return costs[z] < costs[e.z];
    }
};

vector<Edge> edges;
TreeInfo signatures[43211];

int find(vector<int>& G, int x) {
    if (G[x] == x)
        return G[x];

    return G[x] = find(G, G[x]);
}

void combine(vector<int>& G, vector<int>& T, int x, int y) {
    x = find(G, x); y = find(G, y);

    if (T[x] <= T[y]) {
        swap(x, y);
    }

    G[y] = G[x];
    T[x] += T[y];
}

int getSignature() {
    int result = 0;
    vector<pair<ll, int>> pairs;

    for (int i = 0; i < 5; i++) {
        pairs.emplace_back(costs[i], i);
    }

    std::sort(pairs.begin(), pairs.end());

    for (auto& [a, b] : pairs) {
        result = result * 10 + b;
    }

    return result;
}

void analyse(int sign) {
    signatures[sign].init = 1;
    int count = 0, offset = 0;

    // Union-Find
    vector<int> G(N + 1), T(N + 1);

    for (int i = 0; i < N + 1; i++) {
        G[i] = i; T[i] = 1;
    }

    std::sort(edges.begin(), edges.end());

    while (count < N - 1) {
        auto [z, u, v] = edges[offset];
        offset += 1;

        u = find(G, u); v = find(G, v);

        if (u == v)
            continue;

        signatures[sign].e[z] += 1;
        count += 1;

        combine(G, T, u, v);
    }
}

int main() {
    FAST_IO;
    cin >> N >> M >> Q;

    while (M--) {
        int u, v; char z; cin >> u >> v >> z;
        edges.push_back({z - 'A', u, v});
    }

    while (Q--) {
        for (int i = 0; i < 5; i++) {
            cin >> costs[i];
        }

        int sign = getSignature();
        ll result = 0;

        if (!signatures[sign].init) {
            analyse(sign);
        }

        for (int i = 0; i < 5; i++) {
            result += costs[i] * signatures[sign].e[i];
        }

        cout << result << "\n";
    }

    return 0;
}

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

vector<ll> cells;
stack<ll> edible;

int main() {
    FAST_IO;

    // 1. Input
    int N; cin >> N;

    for (int i = 0; i < N; i++) {
        ll T; cin >> T; cells.push_back(T);
    }

    // 2. Solution
    int i = 0;
    ll cell = 2, time = 0;

    std::sort(cells.begin(), cells.end());

    while (i < N) {
        while (i < N && cell > cells[i]) edible.push(cells[i++]);

        if (cell >= cells.back()) {
            cout << time << "\n";
            return 0;
        }

        if (edible.empty()) {
            cout << "NIE" << "\n";
            return 0;
        }

        cell += edible.top(); edible.pop();
        time++;
    }

    cout << time << "\n";
    return 0;
}

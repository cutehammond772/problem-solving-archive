#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;

int main() {
    FAST_IO;
    int T; cin >> T;

    while (T--) {
        vector<tuple<int, int, int>> queue[2];
        vector<pair<int, int>> orders;

        int N, x, y; cin >> N;

        for (int i = 0; i < N; i++) {
            cin >> x >> y;

            queue[0].emplace_back(x, y, y);
            queue[1].emplace_back(x, -y, y);
        }

        std::sort(queue[0].begin(), queue[0].end());
        std::sort(queue[1].begin(), queue[1].end());

        int px = -1, py = 0, mode = 0;

        for (int i = 0; i < N; i++) {
            auto [qx, qt, qy] = queue[mode][i];

            if (px < qx && py != qy) {
                mode = (mode + 1) % 2;
                auto [nqx, nqt, nqy] = queue[mode][i];

                qx = nqx; qy = nqy;
            }

            orders.emplace_back(qx, qy);
            px = qx; py = qy;
        }

        int M, o; cin >> M;

        while (M--) {
            cin >> o;
            auto& [qx, qy] = orders[o - 1];

            cout << qx << " " << qy << "\n";
        }
    }

    return 0;
}

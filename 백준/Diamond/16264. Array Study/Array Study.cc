#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define OFF 100000

using namespace std;
using ll = long long;

struct query {
    int x, y, k;

    query(const int& x, const int& y, const int& k):
            x(x), y(y), k(k) {}

    bool operator<(const query& q) const {
        if (x / k != q.x / k)
            return x / k < q.x / k;

        return y < q.y;
    }
};

struct study {
    int N, M, K;

    vector<query> queries;
    int arr[100001];

    int current, counts[100001];
    list<int> indexes[200001];

    void init() {
        queries.clear();

        for (int i = 0; i <= 200000; i++)
            indexes[i].clear();

        memset(arr, 0, sizeof arr);
        memset(counts, 0, sizeof counts);

        current = 0;
        N = M = K = 0;
    }

    inline void add(int i, bool left) {
        auto& q = indexes[arr[i] + OFF];

        if (!q.empty()) {
            int prev_size = q.back() - q.front();
            counts[prev_size]--;
        }

        if (left) q.push_front(i);
        else q.push_back(i);

        int size = q.back() - q.front();
        counts[size]++;

        current = max(current, size);
    }

    inline void remove(int i, bool left) {
        auto& q = indexes[arr[i] + OFF];
        int prev_size = q.back() - q.front();

        if (left) q.pop_front();
        else q.pop_back();

        counts[prev_size]--;

        if (!q.empty()) {
            int size = q.back() - q.front();
            counts[size]++;
        }

        // 더 작은 size로 재지정한다.
        while (counts[current] == 0)
            current--;
    }
} s;

int main() {
    FAST_IO;
    int T; cin >> T;

    while (T--) {
        s.init();

        // 1. Input
        cin >> s.N;
        s.K = (int) sqrt(s.N);

        for (int i = 1; i <= s.N; i++) {
            cin >> s.arr[i];

            // arr[i] : arr[0...i]
            s.arr[i] += s.arr[i - 1];
        }

        cin >> s.M;

        for (int i = 0; i < s.M; i++) {
            int x, y;
            cin >> x >> y;

            // 누적합은 sum[Y] - sum[X - 1]이다.
            s.queries.emplace_back(x - 1, y, s.K);
        }

        // 2. Solve
        std::sort(s.queries.begin(), s.queries.end());
        ll result = 0;
        int left = -1, right = -1;

        for (auto& [x, y, k] : s.queries) {
            // 첫 번째 쿼리
            if (left < 0 && right < 0) {
                left = x; right = y;

                for (int i = left; i <= right; i++) s.add(i, false);

                result += s.current;
                continue;
            }

            while (x < left) s.add(--left, true);
            while (right < y) s.add(++right, false);
            while (left < x) s.remove(left++, true);
            while (y < right) s.remove(right--, false);

            result += s.current;
        }

        cout << result << "\n";
    }

    return 0;
}

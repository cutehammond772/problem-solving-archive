#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;

int N, M, K, sqrtN;

struct query {
    int order, x, y;

    query(const int& order, const int& x, const int& y):
            order(order), x(x), y(y) {}

    bool operator<(const query& q) const {
        if (x / sqrtN != q.x / sqrtN)
            return x / sqrtN < q.x / sqrtN;

        return y < q.y;
    }
};

vector<query> queries;
int arr[100001], result[100000];

int current, counts[1000001];
list<int> dq[1000001];

void init() {
    memset(arr, 0, sizeof arr);
    memset(result, 0, sizeof result);
    memset(counts, 0, sizeof counts);

    current = 0;
}

inline void add(int i, bool left) {
    auto& q = dq[arr[i]];

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
    auto& q = dq[arr[i]];
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

int main() {
    FAST_IO; init();

    // 1. Input
    cin >> N >> K;
    sqrtN = (int) sqrt(N);

    for (int i = 1; i <= N; i++) {
        cin >> arr[i];

        // arr[i] : arr[0...i]
        arr[i] = (arr[i] + arr[i - 1]) % K;
    }

    cin >> M;

    for (int i = 0; i < M; i++) {
        int x, y;
        cin >> x >> y;

        // 누적합은 sum[Y] - sum[X - 1]이다.
        queries.emplace_back(i, x - 1, y);
    }

    // 2. Solve
    std::sort(queries.begin(), queries.end());
    int left = -1, right = -1;

    for (auto& [order, x, y] : queries) {
        // 첫 번째 쿼리
        if (left < 0 && right < 0) {
            left = x; right = y;

            for (int i = left; i <= right; i++) add(i, false);

            result[order] = current;
            continue;
        }

        while (x < left) add(--left, true);
        while (right < y) add(++right, false);
        while (left < x) remove(left++, true);
        while (y < right) remove(right--, false);

        result[order] = current;
    }

    for (int i = 0; i < M; i++)
        cout << result[i] << "\n";

    return 0;
}

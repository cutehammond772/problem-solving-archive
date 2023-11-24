#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define OFF 100000

using namespace std;

int N, Q, K;

struct query {
    int order, x, y;

    query(const int& order, const int& x, const int& y):
        order(order), x(x), y(y) {}

    bool operator<(const query& q) const {
        if (x / K != q.x / K)
            return x / K < q.x / K;

        return y < q.y;
    }
};

vector<query> queries;
int arr[100001], result[100000];

// 페인트 밝기의 개수
int current, counts[200001], coc[100001];

void init() {
    memset(arr, 0, sizeof arr);
    memset(result, 0, sizeof result);
    memset(counts, 0, sizeof counts);
    memset(coc, 0, sizeof coc);

    current = 0;
}

inline void add(int x) {
    coc[counts[x + OFF]] -= 1;

    counts[x + OFF] += 1;
    coc[counts[x + OFF]] += 1;

    if (counts[x + OFF] > current)
        current = counts[x + OFF];
}

inline void remove(int x) {
    coc[counts[x + OFF]] -= 1;

    counts[x + OFF] -= 1;
    coc[counts[x + OFF]] += 1;

    if (coc[counts[x + OFF] + 1] == 0 && counts[x + OFF] + 1 == current)
        current--;
}

int main() {
    FAST_IO; init();

    // 1. Input
    cin >> N >> Q;
    K = (int) sqrt(N);

    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < Q; i++) {
        int x, y;
        cin >> x >> y;

        queries.emplace_back(i, x, y);
    }

    // 2. Solve
    std::sort(queries.begin(), queries.end());

    int left = -1, right = -1;

    for (auto& [order, x, y] : queries) {
        // 첫 번째 쿼리
        if (left < 0 && right < 0) {
            left = x; right = y;
            for (int i = x; i <= y; i++) add(arr[i]);

            result[order] = current;
            continue;
        }

        while (left < x) remove(arr[left++]);
        while (x < left) add(arr[--left]);
        while (right < y) add(arr[++right]);
        while (y < right) remove(arr[right--]);

        result[order] = current;
    }

    for (int i = 0; i < Q; i++)
        cout << result[i] << "\n";

    return 0;
}

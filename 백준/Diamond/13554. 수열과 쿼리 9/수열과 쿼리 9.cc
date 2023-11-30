#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

int sqrtN;

struct query {
    int order, x, y, k;

    query(const int& order, const int& x, const int& y, const int& k): order(order), x(x), y(y), k(k) {}

    bool operator<(const query& q) const {
        if (x / sqrtN != q.x / sqrtN)
            return x / sqrtN < q.x / sqrtN;

        return y < q.y;
    }
};

vector<query> queries;
int A[100001], B[100001], AT[100001], BT[100001], AC[100001], BC[100001];

ll results[100000];

void init() {
    memset(AT, 0, sizeof AT);
    memset(BT, 0, sizeof BT);
    memset(AC, 0, sizeof AC);
    memset(BC, 0, sizeof BC);
}

inline ll query(const int* tree, int i) {
    ll total = 0;

    while (i > 0) {
        total += tree[i];
        i &= (i - 1);
    }

    return total;
}

inline void update(int* tree, int i, int x) {
    while (i <= 100000) {
        tree[i] += x;
        i += i & -i;
    }
}

inline void add(int i) {
    update(AT, A[i], 1);
    update(BT, B[i], 1);

    AC[A[i]] += 1;
    BC[B[i]] += 1;
}

inline void remove(int i) {
    update(AT, A[i], -1);
    update(BT, B[i], -1);

    AC[A[i]] -= 1;
    BC[B[i]] -= 1;
}

inline ll total(int k) {
    // a * b <= K에서 둘 중 하나는 sqrt(K) 이하인 점을 이용한다.
    int sqrtK = (int) sqrt(k);
    ll result = 0;

    for (int i = 1; i <= sqrtK; i++) {
        result += (query(BT, k / i) - query(BT, sqrtK)) * AC[i];
    }

    for (int i = 1; i <= sqrtK; i++) {
        result += query(AT, k / i) * BC[i];
    }

    return result;
}

int main() {
    FAST_IO; init();
    int N, M;

    // 1. Input
    cin >> N;
    sqrtN = (int) sqrt(N);

    for (int i = 1; i <= N; i++)
        cin >> A[i];

    for (int i = 1; i <= N; i++)
        cin >> B[i];

    cin >> M;

    for (int i = 0; i < M; i++) {
        int x, y, k;
        cin >> x >> y >> k;

        queries.emplace_back(i, x, y, k);
    }

    // 2. Solve
    std::sort(queries.begin(), queries.end());

    int left = -1, right = -1;

    for (auto &q: queries) {
        // 첫 번째 쿼리
        if (left < 0 && right < 0) {
            left = q.x;
            right = q.y;

            for (int i = left; i <= right; i++) add(i);

            results[q.order] = total(q.k);
            continue;
        }

        while (q.x < left) add(--left);
        while (left < q.x) remove(left++);
        while (q.y < right) remove(right--);
        while (right < q.y) add(++right);

        results[q.order] = total(q.k);
    }

    for (int i = 0; i < M; i++)
        cout << results[i] << "\n";

    return 0;
}

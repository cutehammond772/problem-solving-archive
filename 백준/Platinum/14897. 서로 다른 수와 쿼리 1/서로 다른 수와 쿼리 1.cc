#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
int N, M, K;

struct query {
    int idx, x, y;

    query(int idx, int x, int y): idx(idx), x(x), y(y) {}

    // Mo's
    bool operator<(const query& t) const {
        if (x / K != t.x / K) return x / K < t.x / K;
        return y < t.y;
    }
};

vector<int> seq, cp;
vector<query> queries;
int result[1000000], counts[1000000];

int main() {
    FAST_IO; int a, i, j;

    cin >> N;
    K = (int) sqrt(N);
    memset(result, 0, sizeof result);
    memset(counts, 0, sizeof counts);

    for (int x = 0; x < N; x++) {
        cin >> a;
        seq.push_back(a); cp.push_back(a);
    }

    // 좌표 압축 과정
    sort(cp.begin(), cp.end());
    cp.erase(unique(cp.begin(), cp.end()), cp.end());

    for (int x = 0; x < N; x++)
        seq[x] = (int) (lower_bound(cp.begin(), cp.end(), seq[x]) - cp.begin());

    cin >> M;
    for (int x = 0; x < M; x++) {
        cin >> i >> j;
        queries.emplace_back(x, i - 1, j - 1);
    }

    // Mo's 알고리즘을 사용하기 위한 정렬
    sort(queries.begin(), queries.end());

    // 쿼리 처리
    int count = 0;
    auto [f, p, q] = queries[0];

    // 첫번째 쿼리
    for (int x = p; x <= q; x++) {
        if (!counts[seq[x]]++) count++;
    }

    result[f] = count;

    // 나머지 쿼리
    for (int x = 1; x < M; x++) {
        auto [idx, np, nq] = queries[x];

        while (p < np) if (!--counts[seq[p++]]) count--;
        while (np < p) if (!counts[seq[--p]]++) count++;
        while (nq < q) if (!--counts[seq[q--]]) count--;
        while (q < nq) if (!counts[seq[++q]]++) count++;

        result[idx] = count;
    }

    for(int x = 0; x < M; x++) {
        cout << result[x] << "\n";
    }

    return 0;
}

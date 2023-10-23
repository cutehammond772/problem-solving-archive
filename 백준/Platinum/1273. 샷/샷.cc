#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define LEN 3000000

using namespace std;
using ll = long long;

// 각 높이의 캔의 점수의 누적합
ll sum[LEN + 1], mark[LEN + 2];
int idx[300001];

// 인덱스를 저장하는 트리
int tree[LEN * 4 + 1];

ll score[] = { 1, 2, 5 };

void init(int node, int left, int right) {
    if (left == right) {
        tree[node] = 1;
        return;
    }

    int mid = (left + right) / 2;
    init(node * 2, left, mid);
    init(node * 2 + 1, mid + 1, right);

    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

int query(int index, int node, int left, int right) {
    if (tree[node] == 0)
        return 0;

    if (left == right)
        return left;

    int mid = (left + right) / 2;
    int l = tree[node * 2];

    if (index <= l)
        return query(index, node * 2, left, mid);

    return query(index - l, node * 2 + 1, mid + 1, right);
}

void update(int x, int k, int node, int left, int right) {
    if (!(left <= x && x <= right))
        return;

    if (left == right) {
        tree[node] = k;
        return;
    }

    int mid = (left + right) / 2;
    update(x, k, node * 2, left, mid);
    update(x, k, node * 2 + 1, mid + 1, right);

    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

int main() {
    FAST_IO;
    int N, M, t; cin >> N;

    init(1, 1, LEN);
    memset(sum, 0, sizeof sum);
    memset(mark, 0, sizeof mark);

    for (int i = 1; i <= 300000; i++)
        idx[i] = 1;

    for (auto& i : score) {
        for (int n = 1; n <= N; n++) {
            cin >> t;

            mark[idx[n]] += i;
            mark[idx[n] += t] -= i;
        }
    }

    ll point = 0;

    for (int i = 1; i <= LEN; i++) {
        sum[i] = (point += mark[i]);
    }

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> t;

        int x = query(t, 1, 1, LEN);
        cout << sum[x] << "\n";

        update(x, 0, 1, 1, LEN);
    }

    return 0;
}

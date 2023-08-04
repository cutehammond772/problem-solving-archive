#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr)

using namespace std;

// SCC 형성
vector<int> graph[20002], rev[20002];
vector<int> traversal;

int visited[20002], scc[20002];

inline int trueNode(int x) {
    return x << 1 | 1;
}

inline int falseNode(int x) {
    return x << 1;
}

inline int notNode(int x) {
    return x ^ 1;
}

void traverse(int i) {
    visited[i] = 1;

    for (auto next : graph[i]) {
        if (!visited[next]) traverse(next);
    }

    traversal.push_back(i);
}

void createSCC(int i, int component) {
    visited[i] = 1;
    scc[i] = component;

    for (auto next : rev[i]) {
        if (!visited[next]) createSCC(next, component);
    }
}

// 코사라주 알고리즘을 통해 SCC 생성
void init(int N) {
    memset(visited, 0, sizeof visited);

    // TrueNode, FalseNode 모두 고려
    for (int i = 2; i <= N * 2 + 1; i++) {
        if (!visited[i]) traverse(i);
    }

    memset(visited, 0, sizeof visited);
    reverse(traversal.begin(), traversal.end());

    int component = 1;
    for (auto i : traversal) {
        if (!visited[i]) createSCC(i, component++);
    }
}

int main() {
    FAST_IO;
    int N, M, i, j;
    cin >> N >> M;

    while (M--) {
        cin >> i >> j;

        if (i > 0) i = trueNode(i);
        else i = falseNode(-i);

        if (j > 0) j = trueNode(j);
        else j = falseNode(-j);

        // !i -> j
        graph[notNode(i)].push_back(j);
        rev[j].push_back(notNode(i));

        // !j -> i
        graph[notNode(j)].push_back(i);
        rev[i].push_back(notNode(j));
    }

    // SCC 형성
    init(N);

    for (int x = 1; x <= N; x++) {
        if (scc[trueNode(x)] == scc[falseNode(x)]) {
            cout << "0" << "\n";
            return 0;
        }
    }

    cout << "1" << "\n";
    return 0;
}

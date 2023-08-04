#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr)

#define t(x) ((x) << 1)
#define f(x) (((x) << 1) | 1)
#define convert(x) (x > 0 ? t(x - 1) : f(-(x + 1)))

using namespace std;

// SCC 형성
vector<int> graph[20000], rev[20000];
stack<int> traversal;

int visited[20000], scc[20000];

void traverse(int i) {
    visited[i] = 1;

    for (auto next : graph[i]) {
        if (!visited[next]) traverse(next);
    }

    traversal.push(i);
}

void createSCC(int i, int component) {
    visited[i] = 1;
    scc[i] = component;

    for (auto next : rev[i]) {
        if (!visited[next]) createSCC(next, component);
    }
}

// 코사라주 알고리즘을 통해 SCC 생성
void initSCC(int N) {
    memset(visited, 0, sizeof visited);

    // TrueNode, FalseNode 모두 고려
    for (int i = 0; i < N * 2; i++) {
        if (!visited[i]) traverse(i);
    }

    memset(visited, 0, sizeof visited);
    int component = 1;

    while (!traversal.empty()) {
        int i = traversal.top();
        traversal.pop();

        if (!visited[i]) createSCC(i, component++);
    }
}

int main() {
    FAST_IO;
    int N, M, i, j;
    cin >> N >> M;

    while (M--) {
        cin >> i >> j;
        i = convert(i); j = convert(j);

        // !i -> j
        graph[i ^ 1].push_back(j);
        rev[j].push_back(i ^ 1);

        // !j -> i
        graph[j ^ 1].push_back(i);
        rev[i].push_back(j ^ 1);
    }

    // SCC 형성
    initSCC(N);

    // 2-SAT 충족 여부 판별
    for (int x = 0; x < N; x++) {
        if (scc[t(x)] == scc[f(x)]) {
            cout << "0" << "\n";
            return 0;
        }
    }

    cout << "1" << "\n";

    for (int x = 0; x < N; x++) {
        cout << (scc[t(x)] > scc[f(x)]) << " ";
    }

    cout << "\n";
    return 0;
}

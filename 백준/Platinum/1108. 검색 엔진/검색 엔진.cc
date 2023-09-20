#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using ll = long long;

int nodeID, sccID, linkID;
int sccIDs[1250], checked[1250];

// 점수는 int 범위를 초과할 수 있다.
ll scores[1250];

unordered_map<string, int> idx;
vector<int> graph[1250];
stack<int> creation;

// SCC 형성 시 SCC ID가 큰 것부터 위상정렬된다.
bool cmp(const int& a, const int& b) {
    return sccIDs[a] > sccIDs[b];
}

inline int link(const string& name) {
    if (idx.count(name) == 0) {
        idx[name] = linkID++;
    }

    return idx[name];
}

int createSCC(int node) {
    int id = checked[node] = nodeID++;
    creation.push(node);

    for (int next : graph[node]) {
        if (!checked[next]) id = min(id, createSCC(next));
        else if (!sccIDs[next]) id = min(id, checked[next]);
    }

    if (id == checked[node]) {
        while (true) {
            int top = creation.top(); creation.pop();
            sccIDs[top] = sccID;

            if (top == node) break;
        }

        sccID++;
    }

    return id;
}

void init() {
    linkID = 0;
    nodeID = sccID = 1;

    for (ll& score : scores) score = 1;
    memset(sccIDs, 0, sizeof sccIDs);
    memset(checked, 0, sizeof checked);
}

int main() {
    FAST_IO; init();
    int N; cin >> N;

    // 그래프를 형성한다.
    for (int i = 0; i < N; i++) {
        string node, next; cin >> node;
        link(node);

        int P; cin >> P;
        for (int j = 0; j < P; j++) {
            cin >> next;
            graph[link(next)].push_back(link(node));
        }
    }

    // SCC를 형성한다.
    for (int i = 0; i < linkID; i++) {
        if (!checked[i]) createSCC(i);
    }

    // 위상 정렬을 이용하여 점수를 매긴다.
    vector<int> nodes(linkID);
    iota(nodes.begin(), nodes.end(), 0);
    sort(nodes.begin(), nodes.end(), cmp);

    for (int node : nodes) {
        for (int next : graph[node]) {
            if (sccIDs[node] == sccIDs[next])
                continue;

            scores[next] += scores[node];
        }
    }

    // 결과를 출력한다.
    string result; cin >> result;
    cout << scores[link(result)] << "\n";

    return 0;
}

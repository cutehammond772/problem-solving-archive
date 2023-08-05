#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

#define t(x) ((x) << 1)
#define f(x) ((x) << 1 | 1)
#define convert(x) ((x) > 0 ? t(x) : f(-(x)))

using namespace std;

int discovered[2000], sccIDs[2000];
int nodeID, sccID;

stack<int> traversal;

// 타잔 알고리즘을 통해 SCC 생성
int createSCC(int node, vector<int>* graph) {
    int id = discovered[node] = nodeID++;
    traversal.push(node);

    for (auto next : graph[node]) {
        if (!discovered[next]) id = min(id, createSCC(next, graph));
        else if (!sccIDs[next]) id = min(id, discovered[next]);
    }

    if (id == discovered[node]) {
        while (true) {
            int temp = traversal.top(); traversal.pop();
            sccIDs[temp] = sccID;

            if (temp == node) break;
        }

        sccID++;
    }

    return id;
}

// 변수 초기화
void clearAll() {
    nodeID = sccID = 1;
    memset(sccIDs, 0, sizeof sccIDs);
    memset(discovered, 0, sizeof discovered);
}

bool contradicts(int N) {
    /*
     * 타잔 알고리즘의 경우 SCC 번호의 역순으로 위상 정렬된다.
     * 위상 정렬 시 처음 만나는 노드부터 False로 설정하는 것이 항상 이득이므로,
     * 1번을 무조건 통과시키기 위해서는 !(1)를 먼저 만나야 한다.
     * 즉, !(1)를 포함하는 SCC의 번호가 더 높아야 한다.
     */
    if (sccIDs[t(1)] > sccIDs[f(1)])
        return true;

    for (int x = 1; x <= N; x++) {
        if (sccIDs[t(x)] == sccIDs[f(x)])
            return true;
    }

    return false;
}

int main() {
    FAST_IO;
    int N, M, i, j;

    while (cin >> N >> M) {
        clearAll();
        vector<int> graph[2000];

        while (M--) {
            cin >> i >> j;
            i = convert(i); j = convert(j);

            graph[i ^ 1].push_back(j);
            graph[j ^ 1].push_back(i);
        }

        // 1번 참가자가 될 수 있도록 가상의 조건을 하나 추가한다.
        graph[f(1)].push_back(t(1));

        // SCC를 형성한다.
        for (int x = t(1); x <= f(N); x++) {
            if (!discovered[x]) createSCC(x, graph);
        }

        // 모순 여부를 확인한다.
        if (contradicts(N)) {
            cout << "no" << "\n";
            continue;
        }

        cout << "yes" << "\n";
    }

    return 0;
}

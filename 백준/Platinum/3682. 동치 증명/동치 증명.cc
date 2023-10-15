#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;

struct SCCGraph {
    // SCC를 형성하는 데 필요하다.
    int nodeID = 1, sccID = 1;
    int sccIDs[20001]{0}, checked[20001]{0};

    vector<int> graph[20001];
    stack<int> creation;

    // SCC 그래프의 시작 노드와 끝 노드를 구분한다.
    int startNode = 0, endNode = 0;
    int inDegree[20001]{0}, outDegree[20001]{0};

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

    inline void connect(int x, int y) {
        graph[x].push_back(y);
    }

    int solve(int N) {
        // 1. SCC를 형성한다.
        for (int i = 1; i <= N; i++) {
            if (!checked[i]) createSCC(i);
        }

        // 2. SCC 그래프의 진입 차수와 진출 차수를 센다.
        for (int node = 1; node <= N; node++) {
            for (int next : graph[node]) {
                int sccNode = sccIDs[node], sccNext = sccIDs[next];
                if (sccNode == sccNext) continue;

                outDegree[sccNode]++; inDegree[sccNext]++;
            }
        }

        // 3. 모든 SCC 그래프의 시작 노드와 끝 노드를 센다.
        for (int scc = 1; scc < sccID; scc++) {
            if (inDegree[scc] == 0) startNode++;
            if (outDegree[scc] == 0) endNode++;
        }

        if (sccID - 1 == 1)
            return 0;

        // 4. 그 중 더 큰 것을 반환한다.
        return max(startNode, endNode);
    }
};

int main() {
    FAST_IO;
    int T, n, m, s1, s2; cin >> T;

    while (T--) {
        SCCGraph solver;
        cin >> n >> m;

        while (m--) {
            cin >> s1 >> s2;
            solver.connect(s1, s2);
        }

        cout << solver.solve(n) << "\n";
    }

    return 0;
}

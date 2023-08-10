#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;

#define ht(x) ((x) * 2)
#define hf(x) (ht(x) + 1)
#define vt(x) (2000 + (x) * 2)
#define vf(x) (vt(x) + 1)

int nodes[2000];
int discovered[4000], sccIDs[4000];

stack<int> sccStack;
int nodeID, sccID;

void init() {
    nodeID = sccID = 1;
    memset(nodes, 0, sizeof nodes);
    memset(discovered, 0, sizeof discovered);
    memset(sccIDs, 0, sizeof sccIDs);
}

int createSCC(int node, vector<int>* graph) {
    int id = discovered[node] = nodeID++;
    sccStack.push(node);

    for (auto next : graph[node]) {
        if (!discovered[next])
            id = min(id, createSCC(next, graph));

        else if (!sccIDs[next])
            id = min(id, discovered[next]);
    }

    if (id == discovered[node]) {
        while (true) {
            int top = sccStack.top(); sccStack.pop();
            sccIDs[top] = sccID;

            if (top == node)
                break;
        }

        sccID++;
    }

    return id;
}

bool contradicts(int N, int M) {
    // 가로 도로에서의 모순 여부
    for (int x = 0; x < 2 * N; x += 2) {
        if (sccIDs[x] == sccIDs[x + 1]) return true;
    }

    // 세로 도로에서의 모순 여부
    for (int x = 2000; x < 2000 + 2 * M; x += 2) {
        if (sccIDs[x] == sccIDs[x + 1]) return true;
    }

    return false;
}

int main() {
    FAST_IO;
    int T, N, M, K, x1, y1, x2, y2; cin >> T;

    while (T--) {
        vector<int> graph[4000]; init();
        cin >> N >> M >> K;

        while (K--) {
            cin >> x1 >> y1 >> x2 >> y2;

            if (x1 == x2 && y1 == y2) { // Case 1. 출발점과 도착점이 같은 경우
                continue;
            }

            if (x1 != x2 && y1 == y2) { // Case 2. 하나의 도로로 갈 수 있는 경우
                if (x1 > x2) { // 위쪽으로 이동: (!p)이므로 p -> !p
                    graph[vt(y1 - 1)].push_back(vf(y1 - 1));
                } else { // 아래쪽으로 이동: (p)이므로 !p -> p
                    graph[vf(y1 - 1)].push_back(vt(y1 - 1));
                }
            }

            if (x1 == x2 && y1 != y2) {
                if (y1 > y2) { // 왼쪽으로 이동: (!p)이므로 p -> !p
                    graph[ht(x1 - 1)].push_back(hf(x1 - 1));
                } else { // 오른쪽으로 이동: (p)이므로 !p -> p
                    graph[hf(x1 - 1)].push_back(ht(x1 - 1));
                }
            }

            if (x1 != x2 && y1 != y2) { // Case 3. 두 개의 도로로 갈 수 있는 경우
                // x1 가로도로, y2 세로도로
                int p = (y1 < y2) ? ht(x1 - 1) : hf(x1 - 1);
                int q = (x1 < x2) ? vt(y2 - 1) : vf(y2 - 1);

                // y1 세로도로, x2 가로도로
                int r = (x1 < x2) ? vt(y1 - 1) : vf(y1 - 1);
                int s = (y1 < y2) ? ht(x2 - 1) : hf(x2 - 1);

                // (p ^ q) v (r ^ s) = (p v r) ^ (q v r) ^ (p v s) ^ (q v s)임을 이용한다.
                graph[p ^ 1].push_back(r); graph[r ^ 1].push_back(p);
                graph[q ^ 1].push_back(r); graph[r ^ 1].push_back(q);
                graph[p ^ 1].push_back(s); graph[s ^ 1].push_back(p);
                graph[q ^ 1].push_back(s); graph[s ^ 1].push_back(q);
            }
        }

        // 가로 도로에 대해 SCC 형성
        for (int i = 0; i < 2 * N; i++) {
            if (!discovered[i]) createSCC(i, graph);
        }

        // 세로 도로에 대해 SCC 형성
        for (int i = 2000; i < 2000 + 2 * M; i++) {
            if (!discovered[i]) createSCC(i, graph);
        }

        // 모순 여부 확인
        if (contradicts(N, M)) cout << "No" << "\n";
        else cout << "Yes" << "\n";
    }

    return 0;
}

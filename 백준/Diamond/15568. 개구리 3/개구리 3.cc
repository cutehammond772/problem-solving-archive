#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define fn(i, j) (((i) - 1) * 8 + ((j) - 1) * 2)
#define tn(i, j) (fn(i, j) + 1)
#define opp(n) (((n) % 2) ? (n) - 1 : (n) + 1)
#define fr(n) (((n) / 8) + 1)

using namespace std;

// Input
int N, M;

int frog[3001][5];
int favorite[3001][2];

vector<tuple<int, int, int>> bridge;

// 2-SAT
int result[3001];
vector<int> graph[24000];
int sccIDs[24000], discovered[24000];
stack<int> candidate;

int sccID = 1, nodeID = 1;

// ...[nodes][subject]
vector<int> nodes[3001][5];

int createSCC(int node) {
    int id = discovered[node] = nodeID++;
    candidate.push(node);

    for (auto& next : graph[node]) {
        if (!discovered[next]) {
            id = min(id, createSCC(next));
        } else if (!sccIDs[next]) {
            id = min(id, discovered[next]);
        }
    }

    if (id == discovered[node]) {
        while (true) {
            int top = candidate.top();
            candidate.pop();

            sccIDs[top] = sccID;

            if (top == node)
                break;
        }

        sccID++;
    }

    return id;
}

int main() {
    FAST_IO;

    // 1. Input
    cin >> N >> M;

    // 각 관심사에 대한 흥미도
    for (int i = 1; i <= N; i++) {
        cin >> frog[i][1] >> frog[i][2] >> frog[i][3] >> frog[i][4];
    }

    // 선호하는 연꽃
    for (int i = 1; i <= N; i++) {
        cin >> favorite[i][0] >> favorite[i][1];
    }

    for (int i = 0; i < M; i++) {
        int A, B, T; cin >> A >> B >> T;
        bridge.emplace_back(A, B, T);
    }

    // 2. Modeling

    // 2-1. 각 개구리가 선호하는 연꽃을 고려하기
    // 2-2. 개구리 변수 네 개를 묶기
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= 4; j++) {
            if (favorite[i][0] == favorite[i][1]) {
                nodes[favorite[i][0]][j].push_back(tn(i, j));
                graph[fn(i, j)].push_back(tn(i, j));

                continue;
            }

            nodes[favorite[i][0]][j].push_back(tn(i, j));
            nodes[favorite[i][1]][j].push_back(fn(i, j));
        }

        for (int j = 1; j <= 3; j++) {
            for (int k = j + 1; k <= 4; k++) {
                // (!p v q) ^ (p v !q)
                graph[fn(i, j)].push_back(fn(i, k));
                graph[fn(i, k)].push_back(fn(i, j));
                graph[tn(i, j)].push_back(tn(i, k));
                graph[tn(i, k)].push_back(tn(i, j));
            }
        }
    }

    // 2-3. 한 연꽃에는 하나의 개구리만 있도록 하기
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= 4; j++) {
            int U = (int) nodes[i][j].size();

            // 특정 연꽃을 선호하는 개구리가 없으면 배치 방법이 존재하지 않는다.
            if (U == 0) {
                cout << "NO" << "\n";
                return 0;
            }

            // 선호하는 개구리가 한 마리만 있으면 해당 연못을 무조건 선택해야 한다.
            if (U == 1) {
                int f = nodes[i][j][0];
                graph[opp(f)].push_back(f);
                continue;
            }

            for (int x = 0; x < U - 1; x++) {
                int fx = nodes[i][j][x];

                for (int y = x + 1; y < U; y++) {
                    int fy = nodes[i][j][y];

                    graph[fy].push_back(opp(fx));
                    graph[fx].push_back(opp(fy));
                }
            }
        }

    }

    // 2-4. 통나무 고려하기
    for (auto& [A, B, T] : bridge) {
        for (auto p : nodes[A][T]) {
            for (auto q : nodes[B][T]) {
                // 동일한 개구리는 고려하지 않는다.
                if (fr(p) == fr(q)) continue;

                if (frog[fr(p)][T] != frog[fr(q)][T]) {
                    // (!p v !q)
                    graph[q].push_back(opp(p));
                    graph[p].push_back(opp(q));
                }
            }
        }
    }

    // 3. Analysis
    for (int i = 0; i < N * 8; i++) {
        if (!discovered[i]) createSCC(i);
    }

    // 4. Solution
    for (int i = 0; i < N * 8; i += 2) {
        if (sccIDs[i] == sccIDs[i + 1]) {
            cout << "NO" << "\n";
            return 0;
        }
    }

    cout << "YES" << "\n";

    for (int i = 0; i < N; i++) {
        result[favorite[i + 1][sccIDs[(i * 8) + 1] >= sccIDs[i * 8]]] = i + 1;
    }

    for (int i = 1; i <= N; i++)
        cout << result[i] << " ";

    return 0;
}

#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define tn(x, y) ((x) * 200 + (y) * 2)
#define fn(x, y) (tn(x, y) + 1)

using namespace std;

int frogs[100][4], result[100];
vector<int> graph[20000];
vector<int> ponds[100];

int sscID, nodeID;
stack<int> sscStack;
int sscIDs[20000], discovered[20000];

void init() {
    sscID = nodeID = 1;

    memset(result, 0, sizeof result);
    memset(frogs, 0, sizeof frogs);
    memset(sscIDs, 0, sizeof sscIDs);
    memset(discovered, 0, sizeof discovered);
}

int createSSC(int node) {
    int id = discovered[node] = nodeID++;
    sscStack.push(node);

    for (auto& next : graph[node]) {
        if (!discovered[next]) id = min(id, createSSC(next));
        else if (!sscIDs[next]) id = min(id, discovered[next]);
    }

    if (id == discovered[node]) {
        while (true) {
            int top = sscStack.top(); sscStack.pop();
            sscIDs[top] = sscID;

            if (top == node) break;
        }

        sscID++;
    }

    return id;
}

bool contradicts(int N) {
    for (int i = 0; i < 200 * N; i += 2)
        if (sscIDs[i] == sscIDs[i + 1]) return true;

    return false;
}

int main() {
    FAST_IO; init();
    int N, M, A, B, T; cin >> N >> M;

    // 개구리 정보 입력
    for (int i = 0; i < N; i++) {
        cin >> frogs[i][0] >> frogs[i][1] >> frogs[i][2] >> frogs[i][3];
    }

    // (개구리, 연못) 쌍
    for (int i = 0; i < N; i++) {
        cin >> A >> B;
        A -= 1; B -= 1;

        // 2-SAT 생성 (1): 특정 개구리가 선호하는 연꽃 조건 설정
        if (A == B) {
            // (p v p)
            graph[fn(i, A)].push_back(tn(i, A));
            ponds[A].push_back(i);
        } else {
            // (!p v !q) ^ (p v q)
            graph[tn(i, A)].push_back(fn(i, B)); graph[tn(i, B)].push_back(fn(i, A));
            graph[fn(i, A)].push_back(tn(i, B)); graph[fn(i, B)].push_back(tn(i, A));
            ponds[A].push_back(i); ponds[B].push_back(i);
        }

        // 사용하지 않는 쌍은 항상 False로 설정
        for (int j = 0; j < N; j++) {
            // (!p v !p)
            if (!(j == A || j == B)) {
                graph[tn(i, j)].push_back(fn(i, j));
            }
        }
    }

    for (int i = 0; i < N; i++) {
        int size = (int) ponds[i].size();
        int fx, fy;

        // 2-SAT 생성 (2): 각 조합을 통해 한 개구리만 연못에 들어갈 수 있도록 함 (= 두 마리 이상이 들어갈 수 없음)
        for (int x = 0; x < size - 1; x++) {
            for (int y = x + 1; y < size; y++) {
                fx = ponds[i][x], fy = ponds[i][y];

                // (!p v !q)
                graph[tn(fx, i)].push_back(fn(fy, i)); graph[tn(fy, i)].push_back(fn(fx, i));
            }
        }

        // 후보가 하나만 존재하는 경우 무조건 포함
        if (size == 1) {
            fx = fy = ponds[i][0];

            // (p v p)
            graph[fn(fx, i)].push_back(tn(fy, i));
        }
    }

    for (int i = 0; i < M; i++) {
        int fx, fy;

        cin >> A >> B >> T;
        A -= 1; B -= 1; T -= 1;

        // 2-SAT 생성 (3): 두 연못의 개구리 간 선호도를 비교
        for (int x = 0; x < ponds[A].size(); x++) {
            for (int y = 0; y < ponds[B].size(); y++) {
                fx = ponds[A][x], fy = ponds[B][y];

                if (frogs[fx][T] != frogs[fy][T]) {
                    // (!p v !q)
                    graph[tn(fx, A)].push_back(fn(fy, B)); graph[tn(fy, B)].push_back(fn(fx, A));
                }
            }
        }
    }

    for (int i = 0; i < 200 * N; i++) {
        if (!discovered[i]) createSSC(i);
    }

    if (!contradicts(N)) {
        for (int i = 0; i < 200 * N; i += 2) {
            int pond = i % 200 / 2;

            if ((sscIDs[i] < sscIDs[i + 1]) && !result[pond]) {
                result[pond] = (i / 200) + 1;
            }
        }

        cout << "YES" << "\n";

        for (int i = 0; i < N; i++)
            cout << result[i] << " ";
    }
    else { cout << "NO" << "\n"; }

    return 0;
}

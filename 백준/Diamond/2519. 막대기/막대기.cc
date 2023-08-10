#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
struct stick {
    int x1, y1, x2, y2;
};

#define tn(n, i) ((n) * 6 + (i) * 2)
#define fn(n, i) ((n) * 6 + (i) * 2 + 1)

stick nodes[3000];
vector<int> graph[6000];
int discovered[6000], sccIDs[6000];

stack<int> sccStack;
int nodeID, sccID;

vector<int> omit;

void init() {
    nodeID = sccID = 1;
    memset(discovered, 0, sizeof discovered);
    memset(sccIDs, 0, sizeof sccIDs);
}

int createSCC(int node) {
    int id = discovered[node] = nodeID++;
    sccStack.push(node);

    for (auto next : graph[node]) {
        if (!discovered[next])
            id = min(id, createSCC(next));

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

bool contradicts(int N) {
    for (int x = 0; x < 6 * N; x += 2) {
        if (sccIDs[x] == sccIDs[x + 1]) return true;
    }

    return false;
}

int ccw(int x1, int y1, int x2, int y2, int x3, int y3) {
    int result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3);
    return result > 0 ? 1 : result < 0 ? -1 : 0;
}

bool intersects(int i, int j) {
    stick &s1 = nodes[i], &s2 = nodes[j];

    int c1 = ccw(s1.x1, s1.y1, s1.x2, s1.y2, s2.x1, s2.y1) * ccw(s1.x1, s1.y1, s1.x2, s1.y2, s2.x2, s2.y2);
    int c2 = ccw(s2.x1, s2.y1, s2.x2, s2.y2, s1.x1, s1.y1) * ccw(s2.x1, s2.y1, s2.x2, s2.y2, s1.x2, s1.y2);

    return c1 < 0 && c2 < 0;
}

int main() {
    FAST_IO; init();
    int N, pt, qt, rt, pf, qf, rf;

    cin >> N;

    // 막대기 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 3; j++) {
            stick& node = nodes[i * 3 + j];
            cin >> node.x1 >> node.y1 >> node.x2 >> node.y2;
        }

        // 2-SAT 형성 (1): (p v q) ^ (q v r) ^ (p v r)
        pt = tn(i, 0), qt = tn(i, 1), rt = tn(i, 2);
        pf = fn(i, 0), qf = fn(i, 1), rf = fn(i, 2);

        graph[pf].push_back(qt); graph[qf].push_back(pt);
        graph[qf].push_back(rt); graph[rf].push_back(qt);
        graph[pf].push_back(rt); graph[rf].push_back(pt);
    }

    // 2-SAT 형성 (2): 교차하는 두 막대기에 대해 (!p v !q)
    for (int i = 0; i < 3 * N - 1; i++) {
        for (int j = i + 1; j < 3 * N; j++) {
            if (intersects(i, j)) {
                pt = tn(i / 3, i % 3), qt = tn(j / 3, j % 3);
                pf = fn(i / 3, i % 3), qf = fn(j / 3, j % 3);

                graph[pt].push_back(qf); graph[qt].push_back(pf);
            }
        }
    }

    // SCC 형성
    for (int i = 0; i < 6 * N; i++) {
        if (!discovered[i]) createSCC(i);
    }

    // 모순 여부 확인
    if (contradicts(N)) {
        cout << "-1" << "\n";
        return 0;
    }

    // 제거 대상인 막대기 판별
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 3; j++) {
            if (sccIDs[tn(i, j)] >= sccIDs[fn(i, j)])
                omit.push_back((i * 3 + j) + 1);
        }
    }

    // 막대기 번호 출력
    sort(omit.begin(), omit.end());
    cout << omit.size() << "\n";

    if (!omit.empty()) {
        for (auto node : omit)
            cout << node << " ";

        cout << "\n";
    }

    return 0;
}

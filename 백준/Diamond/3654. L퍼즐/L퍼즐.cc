#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define BLANK 0
#define BLACK 1
#define WHITE 2
#define MAX 1010101

using namespace std;

vector<int> nodes[502][502], graph[MAX];
stack<int> candidate;

int discovered[MAX], sccIDs[MAX];
int puzzle[502][502];

int nodeID, sccID;
int N, M, whiteID;
bool possible = true;

void init() {
    for (int i = 0; i < 502; i++) {
        for (int j = 0; j < 502; j++) {
            puzzle[i][j] = BLANK;
            nodes[i][j] = vector<int>();
        }
    }

    for (int i = 0; i < MAX; i++) {
        graph[i] = vector<int>();
    }

    candidate = stack<int>();
    possible = true;

    nodeID = sccID = 1;
    whiteID = 0;

    memset(discovered, 0, sizeof discovered);
    memset(sccIDs, 0, sizeof sccIDs);
}

int createSCC(int node) {
    int id = discovered[node] = nodeID++;
    candidate.push(node);

    for (auto next : graph[node]) {
        if (!discovered[next])
            id = min(id, createSCC(next));

        else if (!sccIDs[next])
            id = min(id, discovered[next]);
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

void check() {
    for (int i = 0; i < whiteID; i++) {
        if (!discovered[i]) createSCC(i);
    }

    for (int i = 0; i < whiteID; i += 4) {
        int left = i, right = i + 1, top = i + 2, bottom = i + 3;

        if ((sccIDs[left] == sccIDs[right]) || (sccIDs[top] == sccIDs[bottom])) {
            possible = false;
            return;
        }
    }
}

void analyse() {
    // 1. B 기준
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (puzzle[i][j] != BLACK) continue;

            // 1-1. Horizontal
            int left = whiteID, right = whiteID + 1;

            if (puzzle[i][j - 1] == WHITE && puzzle[i][j + 1] == WHITE) {
                nodes[i][j - 1].push_back(left);
                nodes[i][j + 1].push_back(right);
            }

            else if (puzzle[i][j - 1] != WHITE && puzzle[i][j + 1] == WHITE) {
                nodes[i][j + 1].push_back(right);

                // 오른쪽 W가 무조건 들어가야 한다.
                graph[left].push_back(right);
            }

            else if (puzzle[i][j - 1] == WHITE && puzzle[i][j + 1] != WHITE) {
                nodes[i][j - 1].push_back(left);

                // 왼쪽 W가 무조건 들어가야 한다.
                graph[right].push_back(left);
            }

            // 둘 다 불가능한 경우 L퍼즐을 만들 수 없다.
            else {
                possible = false;
                return;
            }

            // 1-2. Vertical
            int top = whiteID + 2, bottom = whiteID + 3;

            if (puzzle[i - 1][j] == WHITE && puzzle[i + 1][j] == WHITE) {
                nodes[i - 1][j].push_back(top);
                nodes[i + 1][j].push_back(bottom);
            }

            else if (puzzle[i - 1][j] != WHITE && puzzle[i + 1][j] == WHITE) {
                nodes[i + 1][j].push_back(bottom);

                // 아래쪽 W가 무조건 들어가야 한다.
                graph[top].push_back(bottom);
            }

            else if (puzzle[i - 1][j] == WHITE && puzzle[i + 1][j] != WHITE) {
                nodes[i - 1][j].push_back(top);

                // 위쪽 W가 무조건 들어가야 한다.
                graph[bottom].push_back(top);
            }

            // 둘 다 불가능한 경우 L퍼즐을 만들 수 없다.
            else {
                possible = false;
                return;
            }

            whiteID += 4;
        }
    }

    // 2. W 기준
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (puzzle[i][j] != WHITE) continue;

            // W가 어떤 B에도 인접하지 않은 경우 L퍼즐을 만들 수 없다.
            if (nodes[i][j].empty()) {
                possible = false;
                return;
            }

            int U = (int) nodes[i][j].size();

            // 2-1. B가 하나인 경우, 이 W는 해당 B를 무조건 선택해야 한다.
            if (U == 1) {
                int v = nodes[i][j][0];
                graph[v ^ 1].push_back(v);

                continue;
            }

            // 2-2. 이들 중 두 개 이상을 만족시키지 않도록 한다.
            for (int x = 0; x < U - 1; x++) {
                int vx = nodes[i][j][x];

                for (int y = x + 1; y < U; y++) {
                    int vy = nodes[i][j][y];

                    // (!x1 v !y1) = y1 -> x2, x1 -> y2
                    graph[vy].push_back(vx ^ 1);
                    graph[vx].push_back(vy ^ 1);
                }
            }
        }
    }
}

int main() {
    FAST_IO;
    int T; cin >> T;

    while (T--) {
        init();

        // 1. Input
        cin >> N >> M;

        int white = 0, black = 0;

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                char c; cin >> c;

                if (c == 'B') { black++; puzzle[i][j] = BLACK; }
                if (c == 'W') { white++; puzzle[i][j] = WHITE; }
                if (c == '.') { puzzle[i][j] = BLANK; }
            }
        }

        if (white != black << 1) {
            cout << "NO" << "\n";
            continue;
        }

        // 2. Analyse
        analyse();

        if (!possible) {
            cout << "NO" << "\n";
            continue;
        }

        // 3. Check
        check();

        cout << (possible ? "YES" : "NO") << "\n";
    }

    return 0;
}

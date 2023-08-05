#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define tn(x, k) (((x) - 1) * 10 + (k) * 2 - 1)
#define fn(x, k) (((x) - 1) * 10 + (k) * 2)

using namespace std;
vector<int> graph[500001];
int discovered[500001], sccIDs[500001], variables[250001], nums[50001];

int nodeID, sccID;

stack<int> traversal;

// 타잔 알고리즘을 통해 SCC 생성
int createSCC(int node) {
    int id = discovered[node] = nodeID++;
    traversal.push(node);

    for (auto next : graph[node]) {
        if (!discovered[next]) id = min(id, createSCC(next));
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
void init() {
    nodeID = sccID = 1;
    memset(sccIDs, 0, sizeof sccIDs);
    memset(discovered, 0, sizeof discovered);
    memset(nums, 0, sizeof nums);

    for (auto& variable : variables) variable = -1;
}

bool contradicts(int N) {
    for (int x = 1; x <= N; x++) {
        int num = nums[x]; if (!num) continue;

        for (int k = 1; k <= 5; k++) {
            if ((sccIDs[tn(x, k)] < sccIDs[fn(x, k)]) ^ (num & 1))
                return true;

            num >>= 1;
        }
    }

    for (int x = 1; x <= N * 10; x += 2) {
        if (sccIDs[x] == sccIDs[x + 1])
            return true;
    }

    return false;
}

int main() {
    FAST_IO; init();
    int N, M, x, y, z, temp;
    char t;

    cin >> N;

    // 1. 2-SAT 형성 (1)
    for (int i = 1; i <= N; i++) {
        cin >> temp; if (!temp) continue;
        nums[i] = temp;

        for (int k = 1; k <= 5; k++) {
            if (temp & 1)
                graph[fn(i, k)].push_back(tn(i, k)); // !a -> a
            else
                graph[tn(i, k)].push_back(fn(i, k)); // a -> !a

            temp >>= 1;
        }
    }

    cin >> M;

    // 2. 2-SAT 형성 (2)
    while (M--) {
        cin >> t >> x >> y >> z;

        for (int k = 1; k <= 5; k++) {
            // bitwise AND
            if (t == '&') {
                if (z & 1) {
                    // 항상 a = 1, b = 1
                    graph[fn(x, k)].push_back(tn(x, k)); // !a -> a
                    graph[fn(y, k)].push_back(tn(y, k)); // !b -> b
                } else {
                    graph[tn(x, k)].push_back(fn(y, k)); // a -> !b
                    graph[tn(y, k)].push_back(fn(x, k)); // b -> !a
                }
            }

            // bitwise OR
            if (t == '|') {
                if (z & 1) {
                    graph[fn(x, k)].push_back(tn(y, k)); // !a -> b
                    graph[fn(y, k)].push_back(tn(x, k)); // !b -> a
                } else {
                    // 항상 a = 0, b = 0
                    graph[tn(x, k)].push_back(fn(x, k)); // a -> !a
                    graph[tn(y, k)].push_back(fn(y, k)); // b -> !b
                }
            }

            z >>= 1;
        }
    }

    // 2. 2-SAT 형성 (3)
    for (int i = 1; i <= N; i++) {
        if (nums[i]) continue;

        // 2-1. 16, 8 중 하나'만' 들어가야 한다.
        graph[tn(i, 4)].push_back(fn(i, 5));
        graph[tn(i, 5)].push_back(fn(i, 4));
        graph[fn(i, 4)].push_back(tn(i, 5));
        graph[fn(i, 5)].push_back(tn(i, 4));

        // 2-2. (16, 4)는 불가능하다.
        graph[tn(i, 3)].push_back(fn(i, 5));
        graph[tn(i, 5)].push_back(fn(i, 3));

    }

    // SCC를 형성한다.
    for (int i = 1; i <= N * 10; i++) {
        if (!discovered[i]) createSCC(i);
    }

    // 모순 여부를 확인한다.
    if (contradicts(N)) {
        cout << 0 << "\n";
        return 0;
    }

    cout << 1 << "\n";

    // 변수에 값을 채워 넣는다.
    for (int i = 1; i <= N; i++) {
        temp = 0;

        for (int k = 1; k <= 5; k++) {
            int correct = (sccIDs[tn(i, k)] < sccIDs[fn(i, k)]);
            if (variables[(i - 1) * 5 + k] < 0) variables[(i - 1) * 5 + k] = correct;

            temp += (variables[(i - 1) * 5 + k] << (k - 1));
        }

        cout << temp << " ";
    }

    return 0;
}

#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define SIZE 500001

using namespace std;
using ll = long long;

vector<int> graph[SIZE], restaurants;
int credits[SIZE];
ll sccCredits[SIZE], accumulation[SIZE];

int nodeID, sccID;
int sccIDs[SIZE], checked[SIZE];
stack<int> sccNodes;

void init() {
    nodeID = sccID = 1;
    memset(sccIDs, 0, sizeof sccIDs);
    memset(checked, 0, sizeof checked);

    memset(credits, 0, sizeof credits);
    memset(sccCredits, 0, sizeof sccCredits);
    memset(accumulation, 0, sizeof accumulation);
}

bool compareSCC(const int& a, const int& b) {
    return sccIDs[a] > sccIDs[b];
}

int createSCC(int node) {
    int id = checked[node] = nodeID++;
    sccNodes.push(node);

    for (int next : graph[node]) {
        if (!checked[next]) id = min(id, createSCC(next));
        else if (!sccIDs[next]) id = min(id, checked[next]);
    }

    if (id == checked[node]) {
        while (true) {
            int top = sccNodes.top(); sccNodes.pop();
            sccIDs[top] = sccID;

            if (top == node) break;
        }

        sccID++;
    }

    return id;
}

void calculate(int N, int S, int P) {
    // SCC를 구성한다.
    for (int i = 1; i <= N; i++) {
        if (!checked[i]) createSCC(i);
    }

    // 각 SCC에 포함된 ATM의 액수를 모두 더해 재구성한다.
    for (int i = 1; i <= N; i++) {
        sccCredits[sccIDs[i]] += credits[i];
    }

    // SCC ID 역순으로 정렬한다. (위상 정렬)
    vector<int> nodes(N);
    iota(nodes.begin(), nodes.end(), 1);
    sort(nodes.begin(), nodes.end(), compareSCC);

    // 시작점에 SCC 현금 누적값을 대입한다.
    // 이후, 시작점이 지나는 경로에만 최대 누적값이 대입된다.
    accumulation[sccIDs[S]] = sccCredits[sccIDs[S]];

    for (int node : nodes) {
        for (int next : graph[node]) {
            if (sccIDs[node] == sccIDs[next])
                continue;

            auto currentCredit = accumulation[sccIDs[node]];
            auto& nextCredit = accumulation[sccIDs[next]];

            // 시작점이 지나는 경로가 아님을 의미한다.
            if (currentCredit == 0)
                continue;

            nextCredit = max(nextCredit, currentCredit + sccCredits[sccIDs[next]]);
        }
    }
}

int main() {
    FAST_IO; init();
    int N, M; cin >> N >> M;

    // 도로 정보를 입력한다.
    for (int i = 1; i <= M; i++) {
        int P, Q; cin >> P >> Q;
        graph[P].push_back(Q);
    }

    // 교차로 당 배치된 ATM의 (현금 액수) 정보를 입력한다.
    for (int i = 1; i <= N; i++) {
        cin >> credits[i];
    }

    int S, P, r; cin >> S >> P;

    // 레스토랑을 입력한다.
    for (int i = 1; i <= P; i++) {
        cin >> r;
        restaurants.push_back(r);
    }

    // 인출할 수 있는 현금 액수를 계산한다.
    calculate(N, S, P);

    // 레스토랑을 모두 탐색하여 최대값을 찾는다.
    ll result = 0;
    for (int restaurant : restaurants) {
        result = max(result, accumulation[sccIDs[restaurant]]);
    }

    cout << result << "\n";
    return 0;
}

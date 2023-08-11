#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define rl(x) (((x) - 1) * 2)
#define bl(x) (((x) - 1) * 2 + 1)

using namespace std;

vector<int> graph[10000];
vector<char> result;

int nodeID, sccID;
int discovered[10000], sccIDs[10000];
stack<int> sccStack;

// SCC 형성
int createSCC(int node) {
    int id = discovered[node] = nodeID++;
    sccStack.push(node);

    for (auto& next : graph[node]) {
        if (!discovered[next]) id = min(id, createSCC(next));
        else if (!sccIDs[next]) id = min(id, discovered[next]);
    }

    if (id == discovered[node]) {
        while (true) {
            int top = sccStack.top(); sccStack.pop();
            sccIDs[top] = sccID;

            if (top == node) break;
        }

        sccID++;
    }

    return id;
}

void init() {
    nodeID = sccID = 1;
    memset(sccIDs, 0, sizeof sccIDs);
    memset(discovered, 0, sizeof discovered);
}

int main() {
    FAST_IO; init();
    int K, N, l, guesses[3];
    char c;

    cin >> K >> N;

    while (N--) {
        for (auto& guess : guesses) {
            cin >> l >> c;
            guess = (c == 'R') ? rl(l) : bl(l);
        }

        // SCC 형성: (x v y) ^ (y v z) ^ (x v z)
        auto& [x, y, z] = guesses;

        graph[x ^ 1].push_back(y); graph[y ^ 1].push_back(x);
        graph[y ^ 1].push_back(z); graph[z ^ 1].push_back(y);
        graph[x ^ 1].push_back(z); graph[z ^ 1].push_back(x);
    }

    for (int i = 0; i < 2 * K; i++) {
        if (!discovered[i]) createSCC(i);
    }

    for (int i = 0; i < 2 * K; i += 2) {
        if (sccIDs[i] == sccIDs[i + 1]) {
            cout << "-1" << "\n";
            return 0;
        }

        if (sccIDs[i] < sccIDs[i + 1])
            result.push_back('R');
        else
            result.push_back('B');
    }

    for (auto& x : result)
        cout << x;

    cout << "\n";
    return 0;
}

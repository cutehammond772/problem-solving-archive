#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define tn(x, i) ((x) * 6 + (i) * 2)
#define fn(x, i) ((x) * 6 + (i) * 2 + 1)

#define CURR 0
#define PREV 1
#define NEXT 2

using namespace std;

inline int convert(char c) {
    if (c == 'A') return 0;
    if (c == 'G') return 1;
    if (c == 'T') return 2;
    if (c == 'C') return 3;

    return -1;
}

inline int count(const string& s) {
    return stoi(s.substr(0, s.size() - 1));
}

struct TwoSat {
    vector<int> sequence;
    vector<int> graph[60000];

    int sscID, nodeID;
    stack<int> sscStack;
    int sscIDs[60000], discovered[60000];

    inline void init(int N) {
        sscID = nodeID = 1;
        memset(sscIDs, 0, sizeof sscIDs);
        memset(discovered, 0, sizeof discovered);

        // 2-SAT 생성 (1): 한 베이스는 세가지 Transformation 중 하나만 선택 가능하다.
        for (int x = 0; x < N; x++) {
            // (!prev v !curr)
            graph[tn(x, PREV)].push_back(fn(x, CURR)); graph[tn(x, CURR)].push_back(fn(x, PREV));

            // (!curr v !next)
            graph[tn(x, CURR)].push_back(fn(x, NEXT)); graph[tn(x, NEXT)].push_back(fn(x, CURR));

            // (!prev v !next)
            graph[tn(x, PREV)].push_back(fn(x, NEXT)); graph[tn(x, NEXT)].push_back(fn(x, PREV));
        }

        // 2-SAT 생성 (2): 연속적인 위치에서의 염기 수정은 불가능하다.
        for (int x = 0; x < N - 1; x++) {
            // (!0prev v !1prev)
            graph[tn(x, PREV)].push_back(fn(x + 1, PREV)); graph[tn(x + 1, PREV)].push_back(fn(x, PREV));

            // (!0next v !1next)
            graph[tn(x, NEXT)].push_back(fn(x + 1, NEXT)); graph[tn(x + 1, NEXT)].push_back(fn(x, NEXT));

            // (!0prev v !1next)
            graph[tn(x, PREV)].push_back(fn(x + 1, NEXT)); graph[tn(x + 1, NEXT)].push_back(fn(x, PREV));

            // (!0next v !1prev)
            graph[tn(x, NEXT)].push_back(fn(x + 1, PREV)); graph[tn(x + 1, PREV)].push_back(fn(x, NEXT));
        }
    }

    // 2-SAT 생성 (3): 두 베이스가 동일하도록 조건을 추가한다.
    inline void validatePalindrome(int x, int y) {
        int bx = sequence[x], by = sequence[y];

        // Case 1.
        if (bx == by) {
            // (!x_prev v y_prev)
            graph[tn(x, PREV)].push_back(tn(y, PREV)); graph[fn(y, PREV)].push_back(fn(x, PREV));

            // (x_prev v !y_prev)
            graph[fn(x, PREV)].push_back(fn(y, PREV)); graph[tn(y, PREV)].push_back(tn(x, PREV));

            // (!x_curr v y_curr)
            graph[tn(x, CURR)].push_back(tn(y, CURR)); graph[fn(y, CURR)].push_back(fn(x, CURR));

            // (x_curr v !y_curr)
            graph[fn(x, CURR)].push_back(fn(y, CURR)); graph[tn(y, CURR)].push_back(tn(x, CURR));

            // (!x_next v y_next)
            graph[tn(x, NEXT)].push_back(tn(y, NEXT)); graph[fn(y, NEXT)].push_back(fn(x, NEXT));

            // (x_next v !y_next)
            graph[fn(x, NEXT)].push_back(fn(y, NEXT)); graph[tn(y, NEXT)].push_back(tn(x, NEXT));
        }

        // Case 2.
        if ((bx + 1) % 4 == by) {
            // !x_prev
            graph[tn(x, PREV)].push_back(fn(x, PREV));

            // !y_next
            graph[tn(y, NEXT)].push_back(fn(y, NEXT));

            // (x_next v y_prev)
            graph[fn(x, NEXT)].push_back(tn(y, PREV)); graph[fn(y, PREV)].push_back(tn(x, NEXT));

            // (x_curr v y_curr)
            graph[fn(x, CURR)].push_back(tn(y, CURR)); graph[fn(y, CURR)].push_back(tn(x, CURR));
        }

        // Case 3.
        if ((bx + 2) % 4 == by) {
            // !x_curr
            graph[tn(x, CURR)].push_back(fn(x, CURR));

            // !y_curr
            graph[tn(y, CURR)].push_back(fn(y, CURR));

            // (x_next v y_next)
            graph[fn(x, NEXT)].push_back(tn(y, NEXT)); graph[fn(y, NEXT)].push_back(tn(x, NEXT));

            // (x_prev v y_prev)
            graph[fn(x, PREV)].push_back(tn(y, PREV)); graph[fn(y, PREV)].push_back(tn(x, PREV));
        }

        // Case 4.
        if ((bx + 3) % 4 == by) {
            // !x_next
            graph[tn(x, NEXT)].push_back(fn(x, NEXT));

            // !y_prev
            graph[tn(y, PREV)].push_back(fn(y, PREV));

            // (x_curr v y_curr)
            graph[fn(x, CURR)].push_back(tn(y, CURR)); graph[fn(y, CURR)].push_back(tn(x, CURR));

            // (x_prev v y_next)
            graph[fn(x, PREV)].push_back(tn(y, NEXT)); graph[fn(y, NEXT)].push_back(tn(x, PREV));
        }
    }

    inline void addSequence(char c) {
        sequence.push_back(convert(c));
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

    inline void make(int N) {
        for (int i = 0; i < 6 * N; i++)
            if (!discovered[i]) createSSC(i);
    }

    inline bool contradicts(int N) {
        for (int i = 0; i < 6 * N; i += 2)
            if (sscIDs[i] == sscIDs[i + 1]) return true;

        return false;
    }
};

int main() {
    FAST_IO;
    int N, T;

    while (true) {
        char base; int index, size;
        string subset;
        TwoSat sat;

        cin >> N >> T;
        if (!(N | T)) break;

        // 초기화 & 기본 조건 추가
        sat.init(N);

        // 염기 서열 입력
        for (int i = 0; i < N; i++) {
            cin >> base; sat.addSequence(base);
        }

        // 각 회문 입력
        for (int i = 0; i < T; i++) {
            vector<int> palindrome;
            cin >> subset;

            for (int j = 0; j < (size = count(subset)); j++) {
                cin >> index; palindrome.push_back(index);
            }

            // 각 회문에 대해 2-SAT 생성
            for (int j = 0; j < size / 2; j++) {
                sat.validatePalindrome(palindrome[j], palindrome[(size - 1) - j]);
            }
        }

        sat.make(N);
        if (!sat.contradicts(N)) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }

    return 0;
}

#include <iostream>
#include <ext/rope>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using namespace __gnu_cxx;

// 버전 관리
vector<crope> version;

// 출력한 c의 개수
int d = 0;

int main() {
    FAST_IO; int T; cin >> T;

    // version 0
    version.emplace_back("");

    while (T--) {
        int cmd; cin >> cmd;

        // 1. 문자열 삽입
        if (cmd == 1) {
            int p; string s; cin >> p >> s;

            crope rp(version.back());
            rp.insert(p - d, s.c_str());

            version.push_back(rp);
        }

        // 2. 문자열 제거
        if (cmd == 2) {
            int p, c; cin >> p >> c;

            crope rp(version.back());
            rp.erase((p - 1) - d, c - d);

            version.push_back(rp);
        }

        // 3. 문자열 출력
        if (cmd == 3) {
            int v, p, c; cin >> v >> p >> c;
            crope rp = version[v - d].substr((p - 1) - d, c - d);

            for (char ch : rp) {
                d += (ch == 'c');
                cout << ch;
            }

            cout << "\n";
        }
    }

    return 0;
}

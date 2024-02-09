#include <iostream>
#include <ext/rope>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using namespace __gnu_cxx;

int main() {
    FAST_IO;
    int T; cin >> T;

    while (T--) {
        string s, cmd; cin >> s;
        crope rp(s.c_str());

        do {
            cin >> cmd;

            // 1. 문자열 삽입
            if (cmd == "I") {
                string r; int x; cin >> r >> x;
                rp.insert(x, r.c_str());
            }

            // 2. 문자열 출력
            if (cmd == "P") {
                int x, y; cin >> x >> y;
                cout << rp.substr(x, y - x + 1) << "\n";
            }

        } while (cmd != "END");
    }
    
    return 0;
}

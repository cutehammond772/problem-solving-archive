#include <iostream>
#include <ext/rope>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;
using namespace __gnu_cxx;

// 로프
crope r;

int main() {
    FAST_IO;

    // 입력 문자열을 로프에 추가
    string s; cin >> s;
    r.append(s.c_str());

    // 쿼리 처리
    int Q, C, x, y; cin >> Q;

    while (Q--) {
        cin >> C;

        // 1. 문자열을 가장 앞으로 옮긴다.
        if (C == 1) {
            cin >> x >> y;

            crope frag = r.substr(x, y - x + 1);

            r.erase(x, y - x + 1);
            r.insert(0, frag);
        }

        // 2. 문자열을 가장 뒤로 옮긴다.
        if (C == 2) {
            cin >> x >> y;

            crope frag = r.substr(x, y - x + 1);

            r.erase(x, y - x + 1);
            r.append(frag);
        }

        // 3. 특정 문자를 출력한다.
        if (C == 3) {
            cin >> x;
            cout << r[x] << "\n";
        }
    }

    return 0;
}

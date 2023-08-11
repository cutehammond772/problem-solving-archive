#include <bits/stdc++.h>
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

using namespace std;

int main() {
    FAST_IO;
    int N, P, result = 0; cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> P;
        result ^= P;
    }

    if (result) cout << "koosaga";
    else cout << "cubelover";

    return 0;
}

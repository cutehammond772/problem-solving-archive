#include <iostream>
#include <unordered_map>

using namespace std;

void solve(int* arr, int pos, int count, unordered_map<int, int>& map) {
	if (pos > 100)
		return;

	if (arr[pos] <= count)
		return;

	arr[pos] = count;

	if (map.count(pos) > 0) {
		solve(arr, map[pos], count, map);
	}
	else {
		solve(arr, pos + 1, count + 1, map);
		solve(arr, pos + 2, count + 1, map);
		solve(arr, pos + 3, count + 1, map);
		solve(arr, pos + 4, count + 1, map);
		solve(arr, pos + 5, count + 1, map);
		solve(arr, pos + 6, count + 1, map);
	}
}

int main() {
	int* arr = new int[101]();
	unordered_map<int, int> map;

	int N, M, p, q;
	cin >> N >> M;

	for (int i = 1; i < 101; i++)
		arr[i] = 100;

	for (int i = 0; i < N + M; i++) {
		cin >> p >> q;
		map[p] = q;
	}

	solve(arr, 1, 0, map);
	cout << arr[100] << endl;

	delete[] arr;
	return 0;
}
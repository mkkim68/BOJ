#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int i, j, k = 0;
	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N-i; j++) {
			cout << ' ';
		}
		for (k = 1; k <= i; k++) {
			cout << '*';
		}
		cout << "\n";
	}
	return 0;
}
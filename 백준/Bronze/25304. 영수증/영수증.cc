#include <iostream>
using namespace std;

int main() {
	int X, N, a, b;
	int total = 0;
	cin >> X;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		total += a * b;
	}
	if (total == X) {
		cout << "Yes";
	}
	else {
		cout << "No";
	}
	return 0;
}
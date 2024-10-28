#include <bits/stdc++.h>
using namespace std;

int ReadNumber() {
	int num;
	cout << "Please enter your Number : ";
	cin >> num;
	return num;

}

float CalculateNumebr(int num) {
	return float(num) / 2;
}

void PrintResult(int num) {

	string result = "Half of " + to_string(num) + " is " + to_string(CalculateNumebr(num));
	cout << endl << result << endl;

}


int main() {
	PrintResult(ReadNumber());
}
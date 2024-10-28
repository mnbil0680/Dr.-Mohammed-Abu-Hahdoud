#include <iostream>
using namespace std;

int ReadNumber() {
	int num;
	cout << "Please Enter an integer number : ";
	cin >> num;
	return num;

}

string CheckNumberType(int num) {
	if (num %2) {
		return "odd";
	}
	else {
		return "even";
	}
}

void PrintNumberType(string s) {
	cout << "\nNumber is (" << s << ")";
}

int main() {
	PrintNumberType(CheckNumberType(ReadNumber()));
}
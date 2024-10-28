#include <iostream>
using namespace std;

int ReadMark() {
	int Mark;
	cout << "Please enter your Mark : ";
	cin >> Mark;
	return Mark;
}
string CheckMark(int Mark) {
	if (Mark>=50) {
		return "Pass";
	}
	else {
		return "Fail";
	}
}

void PrintResults(string Status) {
	cout << "\nYou are " << Status;
}
int main() {
	PrintResults(CheckMark(ReadMark()));

}
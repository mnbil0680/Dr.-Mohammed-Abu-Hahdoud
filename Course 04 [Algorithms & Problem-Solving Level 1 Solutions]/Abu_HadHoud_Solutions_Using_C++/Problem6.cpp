#include <iostream>
using namespace std;

struct stInfo {
	string FirstName;
	string LastName;
};

stInfo ReadInfo() {
	stInfo Info;

	cout << "Please Enter your First Name  : ";
	cin >> Info.FirstName;

	cout << "Please enter your Last Name : ";
	cin >> Info.LastName;

	return Info;
}

string GetfullName(stInfo Info) {
	string FullName = Info.FirstName + " " + Info.LastName;
	return FullName;
}

void PrintFullName(string FullName) {
	cout << "\nYour Full Name is  : " << FullName<<endl;
}
int main() {
	PrintFullName(GetfullName(ReadInfo()));
}
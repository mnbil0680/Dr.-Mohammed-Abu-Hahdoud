#include <iostream>
#include <cctype>
using namespace std;
int ReadAge() {
	int age;
	cout << "\nEnter your Age : ";
	cin >> age;
	return age;
}

bool HasDriverLicense() {
	string input;
	cout << "\nDo you have a driver license (yes) or (no) : ";
	cin >> input;
	// to convert ToLower
	for (auto &c : input) {
		c = tolower(c);
	}

	if (input == "yes") {
		return true;
	}
	else {
		return false;
	} 
}

void PrintHireOrRejected(bool HasDriverLicense, int age) {
	if (age >= 21 && HasDriverLicense) {
		cout << "\nHired";
	}
	else {
		cout << "\nRejected";
	}
}

int main() {
	PrintHireOrRejected(HasDriverLicense(), ReadAge());
}
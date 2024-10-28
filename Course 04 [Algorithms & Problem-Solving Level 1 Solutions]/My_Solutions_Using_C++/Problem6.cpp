#include <iostream>
using namespace std;

string ReadLastName() {
	string LastName;
	cout << "Please enter your Last Name : ";
	cin >> LastName;
	return LastName;
}
string ReadFirstName() {
	string FirstName;
	cout << "\nPlaese enter your First Name : ";
	cin >> FirstName;
	return FirstName;
}
void PrintFullName(string FirstName, string LastName) {
	cout << "\nYour Full Name is : " << FirstName << " " << LastName<<"\n\n";
}

int main() {
	string FirstName = ReadFirstName();
	string LastName = ReadLastName();
	PrintFullName(FirstName, LastName);


}
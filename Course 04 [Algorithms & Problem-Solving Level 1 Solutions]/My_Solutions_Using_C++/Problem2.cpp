#include <iostream>
#include <string>
using namespace std;

string ReadName() {
	string Name;
	cout << "Please enter your Name : ";
	cin.ignore(0, '\n');
	getline(cin, Name);
	return Name;
}


void PrintName(string Name){ 
	cout << "\nYour Name is " << "\"" << Name <<"\"" << endl;
}

int main() {

	PrintName(ReadName());

}

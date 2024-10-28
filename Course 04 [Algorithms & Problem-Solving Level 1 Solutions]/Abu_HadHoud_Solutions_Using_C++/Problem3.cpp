#include <iostream>
using namespace std;

enum enNumberType { odd = 1, even =2 };
int ReadNumber() {
	int num;
	cout << "Please enter your  number : ";
	cin >> num;
	return num;
}
enNumberType CheckNumberType(int num) {
	int Result = num % 2;
	if (Result == 0) {
		return enNumberType::even;
	}
	else {
		return enNumberType::odd;
	}

}
void PrintNumberType(enNumberType NumberType) {
	if (NumberType == enNumberType::even) 
		cout << "\n Number is Even. \n";
	else 
		cout << "\n Number is Odd. \n";
	
}
int main() {
	PrintNumberType(CheckNumberType(ReadNumber()));
}
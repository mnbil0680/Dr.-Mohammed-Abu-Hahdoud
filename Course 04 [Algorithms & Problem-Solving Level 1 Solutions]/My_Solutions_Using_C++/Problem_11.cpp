#include <iostream>
using namespace std;

void ReadNumbers(int& Num1, int& Num2 , int& Num3) {
	cout << "Please enter Number 1 : ";
	cin >> Num1;

	cout << "\nPlease enter Number 2 : ";
	cin >> Num2;


	cout << "\nPlease enter Number 3 : ";
	cin >> Num3;

}

int Sumof3Numbers(int n1, int n2, int n3) {
	return n1 + n2 + n3;
}

float CalculateAverage(int sum) {
	return sum / 3.0;
}

string CheckAverage(int sum) {
	if (CalculateAverage(sum) >= 50)
		return "\n\nYou Passed\n\n";
	else
		return "\n\nYou Failed\n\n";
}

void PrintResult(string status) {
	cout << status;
}
int main() {
	int Num1, Num2, Num3;
	ReadNumbers(Num1, Num2, Num3);
	PrintResult(CheckAverage(Sumof3Numbers(Num1, Num2, Num3)));
}
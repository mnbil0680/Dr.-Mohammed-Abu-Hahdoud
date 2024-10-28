#include <bits/stdc++.h>
using namespace std;

void ReadNumbers(int& Num1, int& Num2, int& Num3) {
	cout << "\nPlease enter your Number 1 : ";
	cin >> Num1;

	cout << "\nPlease enter your Number 2 : ";
	cin >> Num2;

	cout << "\nPlease enter your Number 3 : ";
	cin >> Num3;
}

int SumOf3Numbers(int Num1, int Num2, int Num3) {
	return Num1 + Num2 + Num3;
}

void PrintResult(int Total) {
	cout << "\nThe total sum of Numbers si  : " << Total;
}

int main() {
	int Num1, Num2, Num3;
	ReadNumbers(Num1, Num2, Num3);
	PrintResult(SumOf3Numbers(Num1, Num2, Num3));

}
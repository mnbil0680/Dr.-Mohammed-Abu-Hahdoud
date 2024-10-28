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

float CalculateAverage(int Num1, int Num2, int Num3) {
	return SumOf3Numbers( Num1,  Num2, Num3) / 3.0;
}

void PrintResult(float Total) {
	cout << "\nThe total sum of Numbers is  : " << Total;
}

int main() {
	int Num1, Num2, Num3;
	ReadNumbers(Num1, Num2, Num3);
	PrintResult(CalculateAverage(Num1, Num2, Num3));

}
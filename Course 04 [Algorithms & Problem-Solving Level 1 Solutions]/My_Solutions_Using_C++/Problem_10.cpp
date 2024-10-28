#include <iostream>
using namespace std;

struct stNum {
	int Num1;
	int Num2;
	int Num3;
};

stNum ReadNumbers() {
	stNum num;
	cout << "\nPlease enter 1st Number : ";
	cin >> num.Num1;

	cout << "\nPlease enter 2nd Number : ";
	cin >> num.Num2;

	cout << "\nPlease enter 3rd Number : ";
	cin >> num.Num3;

	return num;

}

float Sum3Numbers(stNum Num) {
	return float(Num.Num1 + Num.Num2 + Num.Num3);
}
float Average3Numbers(stNum Num) {
	;
	float avg = Sum3Numbers(Num) / 3;
	return avg;
}
void PrintResult(float avg) {
	cout << "\nSum of 3 numbers is : " << avg;
}


int main() {
	PrintResult(Average3Numbers(ReadNumbers()));
}
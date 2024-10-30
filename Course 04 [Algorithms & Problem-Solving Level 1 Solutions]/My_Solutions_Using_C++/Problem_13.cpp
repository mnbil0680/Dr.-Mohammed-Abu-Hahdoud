#include <iostream>
using namespace std;

void ReadNumbers(int& Num1 , int& Num2, int& Num3) {
	cout << "Enter Number 1 : ";
	cin >> Num1;

	cout << "Enter Number 2 : ";
	cin >> Num2;

	cout << "Enter Number 3 : ";
	cin >> Num3;

}

int MaxOf2Numbers(int n1,int n2, int n3) {
	if (n1 >= n2 && n1 >= n3)
		return n1;
	else if (n2 >= n1 && n2 >= n3)
		return n2;
	else
		return n3;
}

void PrintResult(int max) {
	cout << "\nMax of 3 numbers is : " << max<< endl;
}

int main() {
	int num1, num2, num3;
	ReadNumbers(num1, num2, num3);
	PrintResult(MaxOf2Numbers(num1, num2, num3));
}
#include <iostream>
using namespace std;

void ReadNumbers(int& Num1 , int& Num2) {
	cout << "Enter Number 1 : ";
	cin >> Num1;

	cout << "Enter Number 2 : ";
	cin >> Num2;

}

int MaxOf2Numbers(int n1,int n2) {
	if (n1 >= n2)
		return n1;
	else
		return n2;
}

void PrintResult(int max) {
	cout << "\nMax of 2 numbers is : " << max<< endl;
}

int main() {
	int num1, num2;
	ReadNumbers(num1, num2);
	PrintResult(MaxOf2Numbers(num1, num2));
}
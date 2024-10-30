#include <iostream>
using namespace std;

void ReadNumbers(int& Num1 , int& Num2) {
	cout << "Enter Number 1 : ";
	cin >> Num1;

	cout << "Enter Number 2 : ";
	cin >> Num2;

}

void Swapp(int& n1 , int& n2) {
	int temp = n1;
	n1 = n2;
	n2 = temp;

}

void PrintResult(int num1, int num2) {
	cout << "\nnum 1  = " << num1;
	cout << "\nnum 2  = " << num2;
}

int main() {
	int NUM1, NUM2;
	ReadNumbers(NUM1, NUM2);
	cout << "\nBefore Swapping : \n";
	PrintResult(NUM1, NUM2);
	cout << "\n\nAfter Swapping : \n";
	Swapp(NUM1, NUM2);
	PrintResult(NUM1, NUM2);

}
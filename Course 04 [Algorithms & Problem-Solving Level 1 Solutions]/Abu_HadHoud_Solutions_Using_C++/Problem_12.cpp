#include <iostream>
using namespace std;
void ReadNumbers(int& Num1, int &Num2 ) {
	cout << "Please enter number 1 : ";
	cin >> Num1;

	cout << "Please enter number 2 : ";
	cin >> Num2;

}
int MaxOf2Numbers(int Num1 , int Num2){

	if (Num1 > Num2)
		return Num1;
	else
		return Num2;
	
}

void PrintResults(int Max) {
	cout << "The maximum number is : " << Max << endl;
}
int main() {
	int Num1, Num2;
	ReadNumbers(Num1, Num2);
	PrintResults(MaxOf2Numbers(Num1, Num2));
}
#include <iostream>
using namespace std;

void ReadNumbers(float& A , float& B) {
	cout << "Enter Number A : ";
	cin >> A;

	cout << "Enter Number b : ";
	cin >> B;

}

float CalculateRectangleArea(float A, float B) {
	return A * B;
}

void PrintResult(float Area) {
	cout << "Rectangle Area = " << Area;
}

int main() {
	float A, B;
	ReadNumbers(A, B);
	
	PrintResult(CalculateRectangleArea(A,B));
	

}
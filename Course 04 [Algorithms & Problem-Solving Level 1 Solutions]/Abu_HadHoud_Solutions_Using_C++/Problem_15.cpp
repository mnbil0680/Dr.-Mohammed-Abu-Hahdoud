#include <iostream>
using namespace std;

void ReadNumbers(float& A , float& B) {
	cout << "Please enter Rectangle width A : ";
	cin >> A;

	cout << "Please enter Rectangle length B : ";
	cin >> B;

}

float CalculateRectangleArea(float A, float B) {
	return A * B;
}

void PrintResult(float Area) {
	cout << "\nRectangle Area = " << Area;
}

int main() {
	float A, B;
	ReadNumbers(A, B);
	
	PrintResult(CalculateRectangleArea(A,B));
	

}
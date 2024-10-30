#include <iostream>
using namespace std;
void ReadNumbers(int& A, int& B, int& C ) {
	cout << "Please enter number A : ";
	cin >> A;

	cout << "Please enter number B : ";
	cin >> B;

	cout << "Please enter number C : ";	
	cin >> C;	
}
int MaxOf3Numbers(int A , int B, int C){

	if(A>B)
		if(A>C)
			return A;
		else
			return C;	
	else
		if(B>C)
			return B;
		else
			return C;
}

void PrintResults(int Max) {
	cout << "The maximum number is : " << Max << endl;	
}
int main() {
	int A, B,C;
	ReadNumbers(A, B, C);
	PrintResults(MaxOf3Numbers(A, B, C));
}
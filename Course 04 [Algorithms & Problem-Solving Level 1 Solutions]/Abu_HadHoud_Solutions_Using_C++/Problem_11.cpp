#include <iostream>
using namespace std;
enum enPassFail {Pass = 1, Fail =2 };
void ReadNumbers(int& Mark1, int& Mark2, int& Mark3) {
	cout << "Please enter mark 1 : ";
	cin >> Mark1;

	cout << "Please enter mark 2 : ";
	cin >> Mark2;

	cout << "Please enter mark 3 : ";
	cin >> Mark3;
}

int SumOf3Marks(int Mark1, int Mark2, int Mark3) {
	return Mark1 + Mark2 + Mark3;
}
float CalculateAverage(int Mark1, int Mark2, int Mark3) {
	return SumOf3Marks(Mark1, Mark2, Mark3)/3.0;
}
enPassFail CheckAverage(float Average) {
	if(Average>=50)
		return enPassFail::Pass;
	else
		return enPassFail::Fail;	
}

void PrintResults(float Average) {
	cout << "\nYour average is: " << Average << endl;
	if(CheckAverage(Average)== enPassFail::Pass)
		cout << "You passed" << endl;	
	else
		cout << "You failed" << endl;
}
int main() {
	int Mark1, Mark2, Mark3;
	ReadNumbers(Mark1, Mark2, Mark3);
	PrintResults(CalculateAverage(Mark1, Mark2, Mark3));
}
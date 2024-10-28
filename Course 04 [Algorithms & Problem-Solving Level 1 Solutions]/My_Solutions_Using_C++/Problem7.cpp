#include <iostream>
using namespace std;

float ReadNumber() {
	float Num;
	cout << "Please enter your number : ";
	cin >> Num;
	return Num;

}

float CalculateHalf(float Num) {
	float HalfNum = Num / 2;
	return HalfNum;
}
void PrintResult(float HalfNum) {
	cout << "the orginal number is " << HalfNum * 2 << " and the Half is " << HalfNum << endl;
}

int main() {
	PrintResult(CalculateHalf(ReadNumber()));
}
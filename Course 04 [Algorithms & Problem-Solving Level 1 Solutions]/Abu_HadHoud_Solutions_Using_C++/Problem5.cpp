#include <iostream>
using namespace std;

struct stInfo {
	int Age;
	bool HasDrivingLicense;
	bool HasRecommendation;
};
stInfo ReadInfo() {
	stInfo Info;
	cout << "Please enter your Age : ";
	cin >> Info.Age;

	cout << "Do you have a Driving license : ";
	cin >> Info.HasDrivingLicense;

	cout << "Do you have a Recommendation : ";
	cin >> Info.HasRecommendation;

	return Info;
}

bool IsAccepted(stInfo Info) {
	if (Info.HasRecommendation)
		return true;
	else
		return (Info.Age > 21 && Info.HasDrivingLicense);
}
void PrintResult(stInfo Info) {
	if (IsAccepted(Info))
		cout << "\n Hired";
	else
		cout << "\n Rejected";
}
int main() {
	PrintResult(ReadInfo());
}
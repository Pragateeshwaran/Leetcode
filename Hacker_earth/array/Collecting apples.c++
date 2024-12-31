#include<vector>
#include <iostream>
using namespace std;
int main() {
	int num;
	cin >> num;    //Reading input from STDIN
	// cout << "Input number is " << num << endl;	// Writing output to STDOUT
	while(num--){
		int numFarms, energy;
		vector <int> milk, apple;
		cin >> numFarms >> energy;
		for(int i=0; i<numFarms; i++){
			int temp;
			cin >> temp;
			milk.push_back(temp); 
		}
		for(int i=0; i<numFarms; i++){
			int temp;
			cin >> temp;
			apple.push_back(temp);
		}

		// ============================================================

		int apples = 0; 
		for(int i=0; i<numFarms; i++){
            energy--;
			if(energy != 0){
				apples += apple[i];
			}
			else{
				energy += milk[i];
			}
		}
		cout << apples;
	}
}
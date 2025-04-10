#include<iostream>
using namespace std;

class pattern{
public:
	int y;
public:
	pattern(int x) : y(x) {}
	void print();
};
void pattern :: print(){
	cout<<endl;
	for(int i=1; i<y; i++){
		for(int j=0; j<i; j++)
			cout<<"@";
		cout<<endl;
	}
}
int main(){
	pattern obj(10);
	cout<<obj.y;
	obj.print();
}


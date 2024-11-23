#include<iostream>
#include<vector>
using namespace std;
void print(vector<int> &vec){
    for(int i: vec)
        cout << i<< "\t";
    cout<<endl;
}
vector<int> vec;
int main(){
    vec.push_back(9);
    vec.push_back(91);
    vec.push_back(100);
    vec.push_back(34);
    vec.push_back(365);
    print(vec);
    vec.insert(vec.begin()+3, 10);
    print(vec);
    vec.pop_back();
    print(vec);
    vec.erase(vec.begin());
    print(vec);
    cout << "And the Last Element is " << vec[vec.size()] <<endl;
    cout << &vec << endl;
}
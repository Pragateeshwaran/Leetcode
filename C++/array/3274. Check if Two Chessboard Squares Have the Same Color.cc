#include<iostream>
using namespace std;
class Solution {
public:
    int GetValue(char n){
        return n-'a';
    }
    bool checkTwoChessboards(string coordinate1, string coordinate2) {
        int alpha1 = GetValue(coordinate1[0]);
        int num1   = coordinate1[1] - '1';
        int alpha2 = GetValue(coordinate2[0]);
        int num2   = coordinate2[1] - '1';
        if(((alpha1+num1 )% 2)  == ((num2+alpha2) %2)){
            return 1;
        }
        return 0;
    }
};

int main(){
    Solution obj;
    cout<< obj.checkTwoChessboards("a1", "c3")<<endl;
}
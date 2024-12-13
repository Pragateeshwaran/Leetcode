#include<iostream>
using namespace std;
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result = "";
        while (columnNumber > 0) {
            columnNumber--;
            result = char(columnNumber % 26 + 'A') + result;
            columnNumber /= 26;
        }
        return result;
    }
};
int main(){
    Solution soln;
    cout<<soln.convertToTitle(26)<<endl;
    return 0;
}
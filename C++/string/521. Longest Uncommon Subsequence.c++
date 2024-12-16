#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findLUSlength(string a, string b) {
        if (a == b) {
            return -1; // If the strings are equal, there's no uncommon subsequence
        }
        return max(a.size(), b.size()); // LUS is the length of the longer string
    }
};

int main() {
    Solution soln;
    cout << soln.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef") << endl; // Expected: 17
    cout << soln.findLUSlength("abc", "abc") << endl;                         // Expected: -1
    cout << soln.findLUSlength("abc", "def") << endl;                         // Expected: 3
    cout << soln.findLUSlength("abc", "def") << endl;                         // Expected: 3
    return 0;
}

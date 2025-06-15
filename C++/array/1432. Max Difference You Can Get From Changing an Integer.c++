// You are given an integer num. You will apply the following steps to num two separate times:

//     Pick a digit x (0 <= x <= 9).
//     Pick another digit y (0 <= y <= 9). Note y can be equal to x.
//     Replace all the occurrences of x in the decimal representation of num by y.

// Let a and b be the two results from applying the operation to num independently.

// Return the max difference between a and b.

// Note that neither a nor b may have any leading zeros, and must not be 0.

 

// Example 1:

// Input: num = 555
// Output: 888
// Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
// The second time pick x = 5 and y = 1 and store the new integer in b.
// We have now a = 999 and b = 111 and max difference = 888

// Example 2:

// Input: num = 9
// Output: 8
// Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
// The second time pick x = 9 and y = 1 and store the new integer in b.
// We have now a = 9 and b = 1 and max difference = 8



#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int convertMax(string s) {
        char toReplace = 0;
        for (char c : s) {
            if (c != '9') {
                toReplace = c;
                break;
            }
        }
        if (toReplace)
            replace(s.begin(), s.end(), toReplace, '9');
        return stoi(s);
    }

    int convertMin(string s) {
        char toReplace = 0;

        if (s[0] != '1') {
            toReplace = s[0];
            replace(s.begin(), s.end(), toReplace, '1');
        } else {
            for (int i = 1; i < s.size(); ++i) {
                if (s[i] != '0' && s[i] != '1') {
                    toReplace = s[i];
                    break;
                }
            }
            if (toReplace)
                replace(s.begin(), s.end(), toReplace, '0');
        }
        return stoi(s);
    }

    int maxDiff(int num) {
        string s = to_string(num);
        int high = convertMax(s);
        int low = convertMin(s);
        return high - low;
    }
};

int main() {
    Solution solution;
    int num = 555;
    cout << "Max difference for " << num << ": " << solution.maxDiff(num) << endl;

    num = 9;
    cout << "Max difference for " << num << ": " << solution.maxDiff(num) << endl;

    return 0;
}
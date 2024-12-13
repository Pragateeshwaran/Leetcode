#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool detectCapitalUse(string word) {
        int n = word.size();
        int upperCount = 0;

        for (char c : word) {
            if (c >= 'A' && c <= 'Z') { // Check if the character is uppercase
                upperCount++;
            }
        }

        // Correct capitalization rules
        if (upperCount == n) return true;              // All letters are uppercase
        if (upperCount == 0) return true;              // All letters are lowercase
        if (upperCount == 1 && word[0] >= 'A' && word[0] <= 'Z') return true; // First letter is uppercase

        return false; // Otherwise, the capitalization is incorrect
    }
};

// int main() {
//     Solution soln;
//     cout << soln.detectCapitalUse("USA") << endl;       // Expected: 1 (true)
//     cout << soln.detectCapitalUse("leetcode") << endl; // Expected: 1 (true)
//     cout << soln.detectCapitalUse("Google") << endl;   // Expected: 1 (true)
//     cout << soln.detectCapitalUse("FlaG") << endl;     // Expected: 0 (false)
//     return 0;
// }

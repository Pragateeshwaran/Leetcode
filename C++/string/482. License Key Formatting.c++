#include <iostream>
#include <string>
#include <algorithm> // For std::reverse
using namespace std;

class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        int count = 0;
        string res = "";

        // Traverse the string from the end
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] != '-') { // Ignore dashes
                if (count == k) { // Insert a dash after k characters
                    res += '-';
                    count = 0;
                }
                res += toupper(s[i]); // Convert to uppercase and append
                count++;
            }
        }

        // Reverse the result string to get the correct order
        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
    Solution soln;
    cout << soln.licenseKeyFormatting("5F3Z-2e-9-w", 4) << endl; // Expected: "5F3Z-2E9W"
    cout << soln.licenseKeyFormatting("2-5g-3-J", 2) << endl;    // Expected: "2-5G-3J"
    return 0;
}

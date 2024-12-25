#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        string res = "";
        for (int i = 0; i < s.size(); i++) {
            expand(i, i, s, res);      // Odd-length palindromes
            expand(i, i + 1, s, res); // Even-length palindromes
        }
        return res;
    }

private:
    void expand(int start, int end, string s, string &res) {
        while (start >= 0 && end < s.size() && s[start] == s[end]) {
            start--;  // Move left
            end++;    // Move right
        }
        // Adjust indices to extract the correct substring
        if (end - start - 1 > res.size()) {
            res = s.substr(start + 1, (end - 1) - (start + 1) + 1 );
        }
    }
};

int main() {
    Solution soln;
    cout << soln.longestPalindrome("babad") << endl;
    return 0;
}

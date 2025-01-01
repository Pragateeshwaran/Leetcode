#include <iostream>

using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int ones = count(s.begin(), s.end(), '1');
        
        int ans = 0;
        int zeros = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] == '1') {
                ones--;
            } else {
                zeros++;
            }
            
            ans = max(ans, zeros + ones);
        }
        
        return ans;
    }
};

int main() {
    Solution solution;
    assert(solution.maxScore("011101") == 5);
    assert(solution.maxScore("00111") == 5);
    assert(solution.maxScore("1111") == 3);
    assert(solution.maxScore("00") == 1);
    return 0;
}
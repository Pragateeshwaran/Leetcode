#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> stack; // Simulating a stack to store indices of unmatched '('
        int lastInvalid = -1; // Marks the last invalid index
        int res = 0; // To store the maximum valid length

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stack.push_back(i); // Push the index of '('
            } else {
                if (!stack.empty()) {
                    stack.pop_back(); // Match found, pop the stack
                    if (stack.empty()) {
                        // If the stack is empty, valid substring starts after the last invalid
                        res = max(res, i - lastInvalid);
                    } else {
                        // Valid substring starts after the top of the stack
                        res = max(res, i - stack.back());
                    }
                } else {
                    // If no match is found, mark this index as the last invalid
                    lastInvalid = i;
                }
            }
        }

        return res;
    }
};


int main(){
    Solution soln;
    cout<< soln.longestValidParentheses("(()")<<endl;
    return 0;
}
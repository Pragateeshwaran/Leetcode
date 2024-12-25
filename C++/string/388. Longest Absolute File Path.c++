#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int lengthLongestPath(string input) {
        stack<int> stk;  // Stack to store cumulative lengths of directories
        stk.push(0);     // Initial dummy length
        int maxLen = 0;
        string line;
        int start = 0;
        
        // Process the input manually (splitting by newlines)
        for (int i = 0; i <= input.size(); i++) {
            if (i == input.size() || input[i] == '\n') {
                line = input.substr(start, i - start);  // Get the current line
                start = i + 1;

                // Calculate the level of the current directory/file
                int level = 0;
                while (level < line.size() && line[level] == '\t') {
                    level++;
                }

                // Adjust stack size to match the current level
                while (stk.size() > level + 1) {
                    stk.pop();
                }

                // Current length: previous length + current name length - level + 1 (for '/')
                int len = stk.top() + line.size() - level + 1;
                stk.push(len);

                // Check if it's a file (contains '.')
                if (line.find('.') != string::npos) {   
                    maxLen = (maxLen > len - 1) ? maxLen : len - 1;  // Exclude trailing '/'
                }
            }
        }

        return maxLen;
    }
};

int main() {
    Solution solution;
    string input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext";
    cout << "Longest Path Length: " << solution.lengthLongestPath(input) << endl;
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";
    cout << "Longest Path Length: " << solution.lengthLongestPath(input) << endl;
    return 0;
}

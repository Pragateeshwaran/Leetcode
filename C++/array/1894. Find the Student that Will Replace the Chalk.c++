#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long totalChalkNeeded = 0;
        for (int chalkUse : chalk) {
            totalChalkNeeded += chalkUse;
        }
        
        int remainingChalk = k % totalChalkNeeded;
        cout << remainingChalk << endl;
        
        for (int studentIndex = 0; studentIndex < chalk.size(); studentIndex++) {
            if (remainingChalk < chalk[studentIndex]) {
                return studentIndex;
            }
            remainingChalk -= chalk[studentIndex];
        }
        
        return 0;
    }
};

int main() {
    Solution solution;
    vector<int> chalk = {5, 1, 5};
    int k = 22;
    int result = solution.chalkReplacer(chalk, k);
    cout << "The student that will replace the chalk is at index: " << result << endl;
    return 0;
}
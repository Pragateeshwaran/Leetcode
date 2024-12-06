#include <iostream>
using namespace std;

class Solution {
public:
    bool canAliceWin(int n) {
        // Alice can't start if there are less than 10 stones
        if (n < 10) {
            return false;
        }

        int stonesToRemove = 10;  // Alice starts by removing 10 stones
        bool isAliceTurn = true;   // true means it's Alice's turn, false means it's Bob's turn

        while (n > 0) {
            // If there are fewer stones left than the current player can remove, they lose
            if (n < stonesToRemove) {
                return !isAliceTurn;  // If it's Alice's turn, return false (she loses), else true (Bob loses)
            }

            n -= stonesToRemove;  // Remove the stones from the pile
            stonesToRemove--;      // Decrease the number of stones to be removed in the next turn
            isAliceTurn = !isAliceTurn;  // Toggle turn
        }

        return !isAliceTurn;  // If it's Alice's turn when the loop ends, she loses (return false), otherwise she wins (return true)
    }
};

int main() {
    Solution solution;

    // Test case 1: 12 stones
    int n1 = 12;
    cout << "Can Alice win with " << n1 << " stones? " << (solution.canAliceWin(n1) ? "Yes" : "No") << endl;

    // Test case 2: 1 stone
    int n2 = 1;
    cout << "Can Alice win with " << n2 << " stones? " << (solution.canAliceWin(n2) ? "Yes" : "No") << endl;

    // Test case 3: 20 stones
    int n3 = 20;
    cout << "Can Alice win with " << n3 << " stones? " << (solution.canAliceWin(n3) ? "Yes" : "No") << endl;

    return 0;
}

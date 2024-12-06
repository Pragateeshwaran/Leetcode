#include <iostream>
using namespace std;

class Solution {
public:
    int smallestNumber(int n) {
        // Determine the number of bits in n
        int bits = 0;
        int temp = n;
        while (temp > 0) {
            bits++;
            temp >>= 1; // Right-shift temp to count bits
        }
        
        // Calculate the smallest number with all bits set for the determined number of bits
        int result = (1 << bits) - 1; // 2^bits - 1

        
        return result;
    }
};

int main() {
    Solution solution;
    
    // Test case 1
    int n1 = 5;
    cout << "Smallest number >= " << n1 << " with all set bits: " << solution.smallestNumber(n1) << endl;
    
    // Test case 2
    int n2 = 10;
    cout << "Smallest number >= " << n2 << " with all set bits: " << solution.smallestNumber(n2) << endl;
    
    // Test case 3
    int n3 = 20;
    cout << "Smallest number >= " << n3 << " with all set bits: " << solution.smallestNumber(n3) << endl;

    return 0;
}

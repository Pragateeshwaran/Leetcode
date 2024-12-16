#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // Min-heap to store elements along with their indices
        using Element = pair<int, int>; // {value, index}
        priority_queue<Element, vector<Element>, greater<Element>> minHeap;

        // Push all elements into the heap
        for (int i = 0; i < nums.size(); ++i) {
            minHeap.push({nums[i], i});
        }

        // Perform k operations
        for (int i = 0; i < k; ++i) {
            auto [value, index] = minHeap.top();
            minHeap.pop();

            // Multiply the minimum element by the multiplier
            nums[index] = value * multiplier;

            // Push the updated value back into the heap
            minHeap.push({nums[index], index});
        }

        return nums;
    }
};
int main() {
    Solution soln;
    vector<int> nums = {2, 1, 3, 5, 6};
    vector<int> result = soln.getFinalState(nums, 5, 2);

    // Print the result
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

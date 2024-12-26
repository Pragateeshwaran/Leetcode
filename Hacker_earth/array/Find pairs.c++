#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    int num = 3;
    vector<int> arr = {1, 2, 3};
    

    unordered_map<int, int> countMap;  // Map to store frequency of arr[i] - i
    long long result = 0;

    // Count occurrences of arr[i] - i
    for (int i = 0; i < num; i++) {
        int key = arr[i] - i;  // Compute arr[i] - i
        countMap[key]++;
    }

    // For each key in the map, if it appears more than once, add (k * (k - 1)) / 2 to result
    for (const auto& entry : countMap) {
        int k = entry.second;
        if (k > 1) {
            result += (long long)k * (k - 1) / 2; // Number of ways to choose 2 elements from k elements
        }
    }

    cout << result*2 << endl;
    return 0;
}

#include <iostream>
#include <unordered_set>
#include <string>
#include <algorithm>

class Solution {
public:
    int maxUniqueSplit(std::string s) {
        return backtrack(0, s, std::unordered_set<std::string>());
    }

private:
    int backtrack(int start, const std::string& s, std::unordered_set<std::string> seen) {
        if (start == s.size()) {
            return seen.size();
        }
        
        int max_unique = 0;
        for (int end = start + 1; end <= s.size(); ++end) {
            std::string substring = s.substr(start, end - start);
            if (seen.find(substring) == seen.end()) {
                seen.insert(substring);
                max_unique = std::max(max_unique, backtrack(end, s, seen));
                seen.erase(substring);
            }
        }
        
        return max_unique;
    }
};

int main() {
    Solution soln;
    std::cout << soln.maxUniqueSplit("ababccc") << std::endl;
    std::cout << soln.maxUniqueSplit("aba") << std::endl;
    return 0;
}

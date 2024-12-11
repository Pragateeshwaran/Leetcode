class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> maps;
        if (s.empty()) return 0;  
        
        int res = 0;
        int first_ptr = 0, second_ptr = 0;

        while (second_ptr < s.size()) { 
            if (maps.find(s[second_ptr]) != maps.end() && maps[s[second_ptr]] >= first_ptr) {
                first_ptr = maps[s[second_ptr]] + 1; 
            }
 
            res = max(res, second_ptr - first_ptr + 1);
            maps[s[second_ptr]] = second_ptr;
            second_ptr++;
        }

        return res;
    }
};

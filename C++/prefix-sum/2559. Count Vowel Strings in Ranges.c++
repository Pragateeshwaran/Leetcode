class Solution {
public:
    // Function to check if a character is a vowel
    bool is_vowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    // Function to check if a string is a "vowel string"
    bool is_vowel_string(const string& s) {
        if (s.empty()) return false; // Handle empty strings
        return is_vowel(s.front()) && is_vowel(s.back());
    }

    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n = words.size();
        vector<int> prefix_sum(n + 1, 0);

        // Precompute prefix sums based on whether each word is a "vowel string"
        for (int i = 0; i < n; i++) {
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_string(words[i]);
        }

        vector<int> res;
        for (const auto& query : queries) {
            int l = query[0];
            int r = query[1];
            res.push_back(prefix_sum[r + 1] - prefix_sum[l]);
        }

        return res;
    }
};
int main(){
    Solution solution;
    vector<string> words = {"abc", "aeiou", "abcd", "aeiou", "aeiou"};
    vector<vector<int>> queries = {{0, 2}, {1, 3}, {2, 4}};
    vector<int> res = solution.vowelStrings(words, queries);
    assert(res == vector<int>({0, 2, 3}));
    return 0;
}
#include <iostream>
#include <unordered_map>

struct CharToNumMapper {
    std::unordered_map<char, int> charToNum;

    CharToNumMapper() {
        for (char c = 'a'; c <= 'z'; ++c) {
            charToNum[c] = c - 'a' + 1; // Map 'a' to 1, 'b' to 2, ..., 'z' to 26
        }
    }

    int getValue(char c) {
        if (charToNum.find(c) != charToNum.end()) {
            return charToNum[c];
        } else {
            std::cerr << "Invalid character: " << c << std::endl;
            return -1; // Error value
        }
    }
};

int main() {
    CharToNumMapper mapper;

    // Test the mapper
    char testChar = 'b';
    std::cout << "The value of '" << testChar << "' is: " 
              << mapper.getValue(testChar) << std::endl;

    return 0;
}

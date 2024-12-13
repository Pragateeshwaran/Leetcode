class Solution {
public:
    long long max_returner(std::vector<int>& gifts) {
        int maxi = gifts[0];
        for (auto vals : gifts) {  
            maxi = vals > maxi ? vals : maxi;
        }
        return maxi;
    }

    long long pickGifts(std::vector<int>& gifts, int k) {
        for (int i = 0; i < k; i++) {
            int max_Val = max_returner(gifts); 
            auto it = std::find(gifts.begin(), gifts.end(), max_Val);
            if (it != gifts.end()) {
                gifts.erase(it);  
            }

            int squrt = static_cast<int>(std::pow(max_Val, 0.5));
            gifts.push_back(squrt);
        }

        long long res = 0;
        for (auto n : gifts) {  
            res += n;
            std::cout << n << std::endl;
        }
        return res;
    }
};

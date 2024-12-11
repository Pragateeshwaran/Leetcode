class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int len_prev_incr_seq = 0, len_curr_incr_seq = 0, curr_indx = 0, res = 0;

        while (curr_indx < nums.size()) {
            if (curr_indx == 0 || 
                (curr_indx > 0 && nums[curr_indx - 1] < nums[curr_indx])) {
                len_curr_incr_seq++;
            }
            else {
                len_prev_incr_seq = len_curr_incr_seq;
                len_curr_incr_seq = 1;
            }

            res = max(res, max(len_curr_incr_seq / 2, min(len_curr_incr_seq, len_prev_incr_seq)));
            curr_indx++;
        }

        return res >= k;
    }
};

// O(N)
// O(1)
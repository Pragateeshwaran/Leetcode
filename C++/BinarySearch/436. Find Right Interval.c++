class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<pair<int, int>> startAndIndex;
        vector<int> res(n, -1);
        for(int i=0; i<n; i++){
            int val = intervals[i][0];
            startAndIndex.push_back({val, i});
        }
        
        sort(startAndIndex.begin(), startAndIndex.end());
        
        for(int i=0; i<n; i++){
            int target = intervals[i][1];
            int left = 0;
            int right = n-1;
            int idx = -1;
            while(left <= right){
                int mid = left + (right - left)/2;
                if(target <= startAndIndex[mid].first){
                    idx = startAndIndex[mid].second;
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }
            res[i] = idx;
        }


        return res;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> intervals = {{1, 2}, {2, 3}, {0, 1}};
    vector<int> result = sol.findRightInterval(intervals);
    
    for(int idx : result) {
        cout << idx << " ";
    }
    cout << endl;

    return 0;
}
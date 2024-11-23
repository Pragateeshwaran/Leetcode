class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1 )]
        print(freq)
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for num, counts in count.items():
            print(len(nums), counts)
            freq[counts].append(num)
        print(freq)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res 
        
print(Solution().topKFrequent(nums = [1], k = 1))
print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))


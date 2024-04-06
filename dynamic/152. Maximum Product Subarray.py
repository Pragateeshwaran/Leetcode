class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_sub = min_sub = max_product = nums[0]
        
        for i in nums[1:]:
            if i < 0:
                max_sub, min_sub = min_sub, max_sub
                print("the max_sub",max_sub)
                print("the min_sub",min_sub)
            
            max_sub = max(i, max_sub * i)
            print(max_sub)
            min_sub = min(i, min_sub * i)
            print(min_sub)
            
            max_product = max(max_product, max_sub)
            print(max_product)
        
        return max_product

print(Solution().maxProduct([-1,2,3,-8,4,-3,9]))

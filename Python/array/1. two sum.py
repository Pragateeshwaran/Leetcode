class Solution:
    def twoSum(self, nums, target):
        storage = {}
        for index, element in enumerate(nums):
            # target = x + y
            # x = target - y
            if target - element in storage:
                return [storage[target - element], index]
            storage[element] = index
        return []

obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9)) # [0, 1]
class Solution:
    def twoSum(self, nums, target):
        storage = {}
        for index, element in enumerate(nums):
            if target - element in storage:
                return [storage[target - element], index]
            storage[element] = index
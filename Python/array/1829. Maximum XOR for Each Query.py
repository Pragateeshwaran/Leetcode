class Solution:
    def getMaximumXor(self, nums, maximumBit: int):
        # Calculate the initial XOR of all elements in nums
        current_xor = 0
        for num in nums:
            current_xor ^= num
        
        # max_k is the largest value we can get with maximumBit bits
        max_k = (1 << maximumBit) - 1
        
        # Array to store the answer
        answer = []
        
        # Process each query
        for i in range(len(nums)):
            # Calculate the optimal k for the current current_xor
            k = max_k ^ current_xor
            answer.append(k)
            
            # Remove the last element from nums (simulating by adjusting current_xor)
            current_xor ^= nums[-1 - i]
        
        return answer

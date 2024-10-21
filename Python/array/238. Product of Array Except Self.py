class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        # print(prefix)
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        # print(suffix)
        answer = [prefix[i] * suffix[i] for i in range(n)]
        
        return answer
    
print(Solution().productExceptSelf(nums = [1,2,3,4]))



class Solution:
    def productExceptSelf(self, nums):
        # Count the number of zeros in the array
        zero_count = nums.count(0)

        if zero_count > 1:
            # If there are more than one zero, all products except self will be zero
            return [0] * len(nums)

        # Calculate the total product of all non-zero elements
        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num

        answer = []
        for num in nums:
            if num == 0:
                # If the current element is zero, the product except self is the total product
                answer.append(total_product)
            else:
                # If there is a zero in the array, every other position should be zero
                if zero_count == 1:
                    answer.append(0)
                else:
                    answer.append(total_product // num)

        return answer



print(Solution().productExceptSelf(nums = [1,2,3,4]))
    


### **Understanding the Problem**

# Given an array `nums`, you want to create a new array `answer` where each `answer[i]` is the product of all elements in `nums` **except** `nums[i]`.

# **Example:**

# ```
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# ```

# - For `answer[0]`, it's `2 * 3 * 4 = 24`
# - For `answer[1]`, it's `1 * 3 * 4 = 12`
# - For `answer[2]`, it's `1 * 2 * 4 = 8`
# - For `answer[3]`, it's `1 * 2 * 3 = 6`

# ### **Using Prefix and Suffix Arrays**

# To achieve this without division, we use two auxiliary arrays:

# 1. **Prefix Array (`prefix`)**: 
#    - `prefix[i]` will store the product of all elements to the **left** of index `i`.
   
# 2. **Suffix Array (`suffix`)**:
#    - `suffix[i]` will store the product of all elements to the **right** of index `i`.

# By multiplying `prefix[i]` and `suffix[i]`, you get the product of all elements except `nums[i]`.

# ### **Step-by-Step Explanation**

# Let's walk through the code you provided with an example to see how it works.

# **Given:**
# ```
# nums = [1, 2, 3, 4]
# n = 4
# ```

# #### **1. Initialize Prefix and Suffix Arrays**

# ```python
# prefix = [1] * n      # [1, 1, 1, 1]
# suffix = [1] * n      # [1, 1, 1, 1]
# ```

# #### **2. Build the Prefix Array**

# ```python
# for i in range(1, n):
#     prefix[i] = prefix[i - 1] * nums[i - 1]
# ```

# - **Iteration 1 (`i = 1`):**
#   - `prefix[1] = prefix[0] * nums[0] = 1 * 1 = 1`
#   - `prefix = [1, 1, 1, 1]`
  
# - **Iteration 2 (`i = 2`):**
#   - `prefix[2] = prefix[1] * nums[1] = 1 * 2 = 2`
#   - `prefix = [1, 1, 2, 1]`
  
# - **Iteration 3 (`i = 3`):**
#   - `prefix[3] = prefix[2] * nums[2] = 2 * 3 = 6`
#   - `prefix = [1, 1, 2, 6]`

# **Resulting Prefix Array:**
# ```
# prefix = [1, 1, 2, 6]
# ```

# **What Does This Mean?**
# - `prefix[0]` = 1 (no elements to the left)
# - `prefix[1]` = 1 (`nums[0]`)
# - `prefix[2]` = 1 * 2 (`nums[0] * nums[1]`)
# - `prefix[3]` = 1 * 2 * 3 (`nums[0] * nums[1] * nums[2]`)

# #### **3. Build the Suffix Array**

# ```python
# for i in range(n - 2, -1, -1):
#     suffix[i] = suffix[i + 1] * nums[i + 1]
# ```

# - **Iteration 1 (`i = 2`):**
#   - `suffix[2] = suffix[3] * nums[3] = 1 * 4 = 4`
#   - `suffix = [1, 1, 4, 1]`
  
# - **Iteration 2 (`i = 1`):**
#   - `suffix[1] = suffix[2] * nums[2] = 4 * 3 = 12`
#   - `suffix = [1, 12, 4, 1]`
  
# - **Iteration 3 (`i = 0`):**
#   - `suffix[0] = suffix[1] * nums[1] = 12 * 2 = 24`
#   - `suffix = [24, 12, 4, 1]`

# **Resulting Suffix Array:**
# ```
# suffix = [24, 12, 4, 1]
# ```

# **What Does This Mean?**
# - `suffix[3]` = 1 (no elements to the right)
# - `suffix[2]` = 4 (`nums[3]`)
# - `suffix[1]` = 3 * 4 (`nums[2] * nums[3]`)
# - `suffix[0]` = 2 * 3 * 4 (`nums[1] * nums[2] * nums[3]`)

# #### **4. Compute the Answer**

# ```python
# answer = [prefix[i] * suffix[i] for i in range(n)]
# ```

# Let's compute each element of `answer`:

# - **`i = 0`:**
#   - `answer[0] = prefix[0] * suffix[0] = 1 * 24 = 24`
  
# - **`i = 1`:**
#   - `answer[1] = prefix[1] * suffix[1] = 1 * 12 = 12`
  
# - **`i = 2`:**
#   - `answer[2] = prefix[2] * suffix[2] = 2 * 4 = 8`
  
# - **`i = 3`:**
#   - `answer[3] = prefix[3] * suffix[3] = 6 * 1 = 6`

# **Final Answer:**
# ```
# answer = [24, 12, 8, 6]
# ```

# ### **Visualization**

# Let's visualize the process with the example `nums = [1, 2, 3, 4]`:

# | Index | nums[i] | Prefix[i]| Suffix[i] | Answer[i] = Prefix[i] * Suffix[i]   |
# |-------|--------|-----------|-----------|-------------------------------------|
# | 0     | 1      | 1         | 24        | 24                                  |
# | 1     | 2      | 1         | 12        | 12                                  |
# | 2     | 3      | 2         | 4         | 8                                   |
# | 3     | 4      | 6         | 1         | 6                                   |

# ### **Why This Works**

# - **Prefix Array:** Accumulates the product of all elements to the **left** of each index.
# - **Suffix Array:** Accumulates the product of all elements to the **right** of each index.
# - By multiplying `prefix[i]` and `suffix[i]`, you effectively get the product of all elements **except** `nums[i]`.

# ### **Advantages**

# - **Time Complexity:** O(n) — You traverse the array three times (once for prefix, once for suffix, and once for the final answer).
# - **Space Complexity:** O(n) — You use two additional arrays (`prefix` and `suffix`). However, this can be optimized to O(1) extra space by modifying the answer array in place.

# ### **Optimizing Space (Optional)**

# If you want to reduce space usage, you can compute the prefix and suffix products on the fly and store them directly in the `answer` array. Here's how:

# ```python
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         answer = [1] * n
        
#         # Compute prefix products and store in answer
#         prefix = 1
#         for i in range(n):
#             answer[i] = prefix
#             prefix *= nums[i]
        
#         # Compute suffix products and multiply with corresponding prefix
#         suffix = 1
#         for i in range(n - 1, -1, -1):
#             answer[i] *= suffix
#             suffix *= nums[i]
        
#         return answer
# ```

# This optimized version uses O(1) extra space (ignoring the output array) by first storing prefix products in `answer` and then multiplying by suffix products in a second pass.

# ### **Conclusion**

# Using prefix and suffix arrays is a powerful technique to solve the "Product of Array Except Self" problem efficiently without using division. By separately computing the products of all elements to the left and right of each index, you can combine these to get the desired product for each position.
class Solution:
    def decodeString(self, s: str) -> str:
        # 1. Keep adding to stack untill you get ]
        # 2. When ] is found, dont add ] to stack, instead pop all characters until [ is found, pop [ too
        # 3. Then keep popping till we have digits, keep adding to k
        # 4. Multiply digit * string popped , and add this new string to stack

        stack=[]
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i]) # 1
            else:
                substr=''
                while stack and stack[-1]!= '[': # 2
                    substr=stack.pop() + substr
                
                stack.pop() # 2. Popping [
                k =''
                while stack and stack[-1].isdigit(): # 3
                    k = stack.pop() + k
                
                stack.append( int(k) * substr  ) # 4
        
        return ''.join(stack) # stack elements will be joined together directly without any characters in between




print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("3[a]2[bc]"))
# print(Solution().decodeString("3[a2[c]]"))
# "accaccacc"
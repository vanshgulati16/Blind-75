class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #stores the product of all the elements before nums[0]
        pre = 1
        #stores the product of all the elements before nums[len(nums)-1] 
        post = 1 
        output = []
        j = len(nums)-1
        # iterating over the nums array and add the prefix to output array and multiplying  the prefix with the nums array element consequetively  
        for i in nums:
            output.append(pre)
            pre = pre*i
        # reversing the list and then iterating over it and then multiplying the postfix with the output elements and then updating the postfix with respetive nums element consequetively 
        while j>=0:
            output[j] = post*output[j]
            print(output[j])
            post = post*nums[j]
            j-=1
        return output
        
# Time complexity: O(N) as using two loops independently.
# Space Complexity: O(N) as using one output array of size N

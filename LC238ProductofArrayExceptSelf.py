# Runtime Complexity O(N)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p) # output 存 nums[0:i-1]的乘积
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p # output 再乘i元素后面的乘积
            p = p * nums[i]
        return output
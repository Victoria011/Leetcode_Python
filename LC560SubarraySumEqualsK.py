# Approach 1 : Time Limit Exceeded
# Runtime Complexity: O(N^2)
# Space Complexity: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        res = [0] * len(nums)
        count = 0
        res[0] = nums[0]
        if res[0] == k:
            count += 1
        for i in range(1,len(nums)):
            res[i] = res[i-1] + nums[i]
            if res[i] == k:
                count+=1

        for j in range(1, len(nums)):
            for r in range(j, len(nums)):
                res[r] = res[r] - nums[j-1]
                if res[r] == k:
                    count+=1
        return count

# Approach 2 : prefix sum
# Runtime Complexity: O()
# Space Complexity: O()
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
		dic = collections.defaultdict(int)
		dic[0] = 1
		res = 0
		sum_i = 0
		for i in range(nums_len):
			sum_i += nums[i] 
			sum_j = sum_i -k
			if sum_j  in dic:
				res += dic[sum_j]
			dic[sum_i] += 1    
		return res
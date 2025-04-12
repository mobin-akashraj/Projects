class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]] = i

nums = [2,7,9,11]
target = 11
result = Solution().twoSum(nums,target)
expected = [0,2]
if result == expected :
    print("success!")
else:
    print("try again")
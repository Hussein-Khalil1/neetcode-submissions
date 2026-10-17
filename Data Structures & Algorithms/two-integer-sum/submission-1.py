class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        first = 0
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i + 1 :]:
                diff = target - nums[i]
                first = nums[i]
                break
        hashmap = {}
        index1 = 0
        index2 = 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i 
        if diff != first:
            index1 = hashmap[first]
            index2 = hashmap[diff]
        else:
            index1 = hashmap[first]
            for i in range(len(nums)):
                if index1 != i and nums[i] == diff:
                    index2 = i

        
        if index1 < index2:
            return [index1, index2]
        else:
            return [index2, index1]
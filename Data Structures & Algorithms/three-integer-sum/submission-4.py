class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:          # smallest number is positive, so no sum can be 0
                break
            if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate first numbers
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1        # need a bigger sum
                elif total > 0:
                    right -= 1       # need a smaller sum
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:   # skip duplicates
                        left += 1

        return result
    

    


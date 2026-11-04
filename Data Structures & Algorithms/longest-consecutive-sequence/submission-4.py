class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #naive solution: 
        if not nums:
            return 0
        
        count = 1
        best = 1
        nums.sort()
        i = 0
        while i < len(nums) -1:
            if nums[i] == nums[i+1] -1: 
                count +=1 
                i +=1 
            elif nums[i] == nums[i+1]:
                i+=1 
            else:
                best = max(count, best)
                count = 1 
                i+=1 
        best = max(count, best)
        return best



            
            


        
        
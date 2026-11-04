class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #optimized solution: O(n) space and time complexity, lfg!
        if not nums:
            return 0 

        hshset = set(nums)
        arr = []
        count = 1
        best = 1

        for num in hshset:
            if num-1 not in hshset: 
                arr.append(num)
        i = 0 
        value = arr[i]
        while i < len(arr):
            if value + 1 in hshset:
                count +=1 
                value += 1
            else:
                i+= 1
                best = max(count, best)
                count = 1
                if i <= len(arr) -1:
                    value = arr[i]

        return best 



                
        

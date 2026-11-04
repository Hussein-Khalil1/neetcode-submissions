import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]
        hsh = {}
        
        for num in nums:
            if num not in hsh:
                hsh[num] = 1
            else:
                hsh[num] += 1

        for key in hsh: 
            i = key
            arr[hsh[key]].append(i)
        result = []
        for i in range(len(arr) -1, 0, -1):
            for n in arr[i]:
                result.append(n)
                if len(result) == k:
                    return result
                
            



            
        


        
                           

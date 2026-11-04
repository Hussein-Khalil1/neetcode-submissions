class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        total = 1
        zeros = 0
        for num in nums:
            if num == 0: 
                zeros += 1
            else:
                total = total * num

        for num in nums:
            if zeros > 1:
                lst.append(0) 
            elif zeros == 1:  
                if num == 0: 
                    lst.append(total) 
                else:
                    lst.append(0)
            else:
                lst.append(total//num)
        
        return lst

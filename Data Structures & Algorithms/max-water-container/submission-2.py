class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        area = 0
        curr = 0 
        while i< j and i !=j:
            curr = min(height[i], height[j]) * (j-i)
            area = max(curr, area)
            if height[i] < height[j]:
                i+=1
            elif height[j] < height[i]:
                j-=1
            else:
                if height[j] < height[j-1]:
                    j-=1
                elif not height[j] < height[j-1] and height[j] != max(height):
                    j-=1
                #missing how about if its the opposite what to do? do we ignore ofc not
                elif height[i] < height[i+1]:
                    i+=1
                elif not height[i] < height[i+1] and height[i] != max(height):
                    i+=1 
                else:
                    return max(area, curr)
        return area

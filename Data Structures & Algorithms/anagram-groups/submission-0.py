class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for e in strs:
            s = "".join(sorted(e))
            if s not in result:
                result[s] = [e]
            else:
                result[s].append(e)
        array = []
        for value in result.values():
            array.append(value)
        return array



                


                


                

                
            
   

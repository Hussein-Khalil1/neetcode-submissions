class Solution:

    def encode(self, strs: List[str]) -> str:
        strings = ""
        for word in strs:
            strings += word 
            strings += "#?"
        return strings
    def decode(self, s: str) -> List[str]:
        lst = s.split("#?")
        lst.pop()
        return lst
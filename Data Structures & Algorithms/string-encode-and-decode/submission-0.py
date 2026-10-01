class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for str in strs:
            encodedStr = f"{str}#20bdaffa"
            encoded+=encodedStr

        return encoded

    def decode(self, s: str) -> List[str]:
        splited = s.split('#20bdaffa')
        splited.pop()
        
        
        return splited
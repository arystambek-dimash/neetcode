class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for j in s:
                res+=f"{ord(j)},"
            res+= " "
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        num = ""
        st = ""
        for ch in s:
            if ch == ",":
                num = int(num)
                st+=chr(num)
                num = ""
            elif ch == " ":
                res.append(st)
                st = ""
            else:
                num+=ch
        return res
                
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        s = []
        while temperatures:
            l = temperatures.pop(0)
            c = 0
            s.append(l)
            for i in temperatures:
                print(l,i)
                if i > l:
                    c += 1
                    res.append(c)
                    c = 0
                    s.pop()
                    break
                else:
                    c+=1 
            print(s)
            if s:
                res.append(0)  
                s.pop()             
        return res 
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d = {chr(i):k+1 for k, i in enumerate(range(ord('a'),ord('z')+1))}
        
        t1 = ''
        for ch in s:
            t1 += str(d[ch])
            
        print(t1)
        
        for i in range(k):
            res = 0
            for ch in t1:
                res += int(ch)
            t1 = str(res)
            
        return res

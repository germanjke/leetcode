class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        list_num = list(map(lambda x: int(x), num))
        larger = False
        
        for i in range(len(list_num)):
            
            cur = change[int(list_num[i])]
            
            if cur > list_num[i]:
                
                list_num[i] = cur
                larger = True
                
            elif (cur == list_num[i] and larger):
                
                continue
                
            elif (cur < list_num[i] and larger):
                
                break
                
        list_num = list(map(lambda x: str(x), list_num))
        
        return ''.join(list_num)

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for x in range(1, n+1):
            if n % x == 0:
                count += 1
                print('x is', x)
            if count == 4:
                return False
        print(count)
        if count == 3:
            return True
          
#brute force

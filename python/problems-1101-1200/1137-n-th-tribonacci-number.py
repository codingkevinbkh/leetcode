'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_map = {}
        tribonacci_map[0] = 0
        tribonacci_map[1] = 1
        tribonacci_map[2] = 1
        
        if n >= 3:
            for i in range(3, n+1):
                tribonacci_map[i] = tribonacci_map[i-1] + tribonacci_map[i-2] + tribonacci_map[i-3]
        
        return tribonacci_map[n]

### solution 2 ###
class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_map = {}
        tribonacci_map[0] = 0
        tribonacci_map[1] = 1
        tribonacci_map[2] = 1
        
        def find_tribonacci(n):
            if n in tribonacci_map:
                return tribonacci_map[n]
            if n-1 not in tribonacci_map:
                tribonacci_map[n-1] = find_tribonacci(n-1)
            if n-2 not in tribonacci_map:
                tribonacci_map[n-2] = find_tribonacci(n-2)
            if n-3 not in tribonacci_map:
                tribonacci_map[n-3] = find_tribonacci(n-3)
            return tribonacci_map[n-1] + tribonacci_map[n-2] + tribonacci_map[n-3]
        
        return find_tribonacci(n)

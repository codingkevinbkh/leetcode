'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        K_bin = bin(K-1)[2:]
        level = N-1
        tree_map = {
            '0': {
                '0': '0',
                '1': '1'
            },
            '1': {
                '0': '1',
                '1': '0'
            }
        }
        
        def find_num(root, path):
            current_leaf = tree_map[root][path[0]]
            if len(path) == 1:
                return current_leaf
            else:
                return find_num(current_leaf, path[1:])
        
        return find_num('0', K_bin.zfill(level))

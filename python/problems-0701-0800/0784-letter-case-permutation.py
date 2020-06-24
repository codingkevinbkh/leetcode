'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        S_len = len(S)

        def permute(sub_str):
            idx = len(sub_str)
            if idx == S_len:
                res.append(sub_str)
                return
            if S[idx].isnumeric():
                permute(sub_str+S[idx])
            else:
                permute(sub_str+S[idx].lower())
                permute(sub_str+S[idx].upper())
                
        permute('')
        return res

### solution 2 ###
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def permute(sub_str):
            if len(sub_str) == 0:
                return ['']
            first_char = sub_str[0]
            str_list = permute(sub_str[1:])
            if first_char.isnumeric():
                return list(map(lambda s: first_char+s, str_list))
            else:
                return list(map(lambda s: first_char.upper()+s, str_list)) + list(map(lambda s: first_char.lower()+s, str_list))
                
        return permute(S)

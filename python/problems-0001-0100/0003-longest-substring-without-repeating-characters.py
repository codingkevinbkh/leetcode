'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = []
        longest = 0
        for idx, char in enumerate(s):
            if char in visited:
                visited = visited[visited.index(char)+1:]
            visited.append(char)
            longest = max(longest, len(visited))
        return longest

### solution 2 ###
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        longest = 0
        left = 0
        for idx, char in enumerate(s):
            if char in char_map:
                left = max(left, char_map[char]+1)
            char_map[char] = idx
            longest = max(longest, idx-left+1)
        return longest

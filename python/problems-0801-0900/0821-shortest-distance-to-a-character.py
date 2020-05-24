'''
歡迎訂閱我們的Youtube頻道Coding Kevin BKH，影片中會使用動畫解釋演算法，同時也有Leetcode實戰解題。
Check out our Youtube channel, we explain the solutions step by step. Please subscribe!
The audio is in Mandarin

Coding Kevin BKH

'''

### solution 1 ###
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pos = [i for i in range(len(S)) if S[i] == C]
        pos_len = len(pos)
        dis = []
        curr = 0
        for i in range(len(S)):
            if curr >= pos_len:
                dis.append(abs(pos[curr-1]-i))
            elif curr-1 < 0:
                dis.append(abs(pos[curr]-i))
            else:
                dis.append(min(abs(pos[curr]-i), abs(pos[curr-1]-i)))
            if curr < pos_len and i == pos[curr]:
                curr += 1
        return dis

### solution 2 ###
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        import math

        dis = []
        prev = None
        for i in range(len(S)):
            if S[i] == C:
                prev = i
            if prev != None:
                dis.append(i-prev)
            else:
                dis.append(math.inf)
        prev = None
        for i in range(len(dis)-1, -1, -1):
            if S[i] == C:
                prev = i
            if prev != None:
                dis[i] = min(prev-i, dis[i])
        return dis

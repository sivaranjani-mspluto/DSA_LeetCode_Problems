from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_window,window={},{}
        for c in t:
            target_window[c]=1 + target_window.get(c,0)

        have,need=0,len(target_window)
        res,min_len=[0,0],float('inf')
        left=0
        for right in range(len(s)):
            ch_r= s[right]
            window[ch_r]=1+window.get(ch_r,0)
            if ch_r in target_window and window[ch_r] == target_window[ch_r]:
                have+=1
            while have == need:
                if min_len>(right-left+1):
                    min_len=(right-left+1)
                    res=[left,right]
                window[s[left]]-=1
                if s[left] in target_window and window[s[left]] < target_window[s[left]]:
                    have-=1
                left+=1
        
        l,r=res
        return s[l:r+1] if min_len != float('inf') else ""
        
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #all requirements
        target_window,window={},{}
        for c in t:
            target_window[c]=1 + target_window.get(c,0)

        have,need=0,len(target_window)
        res,min_len=[0,0],float('inf')
        left=0

        #SLIDING WINDOW
        #EXPAND#
        for right in range(len(s)):
            #update right
            ch_r= s[right]
            window[ch_r]=1+window.get(ch_r,0)
            #update have after right increases
            if ch_r in target_window and window[ch_r] == target_window[ch_r]:
                have+=1
            #if satisfied, shrink till you find a more minimum one
            #SHRINK#
            while have == need:
                #update the most min_length
                if min_len>(right-left+1):
                    min_len=(right-left+1)
                    res=[left,right]
                #reduce the window and move left
                window[s[left]]-=1
                #everytime the window moves update have
                if s[left] in target_window and window[s[left]] < target_window[s[left]]:
                    have-=1
                left+=1
        
        l,r=res
        return s[l:r+1] if min_len != float('inf') else ""
        
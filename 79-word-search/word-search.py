class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path=set()  #to have a list of seen nodes in THAT path # set<tuple>

        def dfs_word_found(r,c,ind):
            if ind==len(word):
                return True
            #conditions for False 
            if (r<0 or c<0 or r>=ROWS or c>=COLS):
                return False
            if ((r,c) in path or board[r][c]!= word[ind] ):
                return False
            
            #match letter found - add as seen 
            path.add((r,c))
            #if anyside had the letter
            res= (dfs_word_found(r+1,c,ind+1) or
                dfs_word_found(r-1,c,ind+1) or
                dfs_word_found(r,c+1,ind+1) or
                dfs_word_found(r,c-1,ind+1)) 

            path.remove((r,c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs_word_found(r,c,0):
                    return True
        return False
        
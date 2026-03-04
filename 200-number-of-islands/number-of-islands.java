class Solution {
    public static void dfs(char[][] grid, int i, int j) {
            int rows= grid.length;
            int cols= grid[0].length;
            if (i < 0 || i >= rows || j < 0 || j >= cols) return;
            if (grid[i][j] != '1') return;   // ← CHANGE '1' per problem
            grid[i][j] = '0';                // mark visited
            //nothing extra is done at each cell
            dfs(grid, i+1, j);
            dfs(grid, i-1, j);
            dfs(grid, i, j+1);
            dfs(grid, i, j-1);
        }

    public int numIslands(char[][] grid) {
        int rows= grid.length;
        int cols= grid[0].length;
        int count = 0;
        for (int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                if(grid[i][j]=='1'){
                    count++;
                    dfs(grid,i,j);
                }
            }
        }
        return count;
    }
}
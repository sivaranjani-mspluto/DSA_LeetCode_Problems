class Solution {
    static boolean bfs(int n , int sc, int dest, List<List<Integer>> adj){
        boolean[] visited=new boolean[n];
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(sc);
        visited[sc]=true;

        while(!queue.isEmpty()){
            int ele = queue.poll();
            if (ele == dest) return true;
            for (int neig : adj.get(ele)) {
                if (!visited[neig]) {
                    visited[neig] = true;
                    queue.offer(neig);
            }
        }
        }
        return false;
    }
    public boolean validPath(int n, int[][] edges, int source, int destination) {
                List<List<Integer>> adj = new ArrayList<>();
                for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
                for (int[] edge : edges) {
                    adj.get(edge[0]).add(edge[1]);
                    adj.get(edge[1]).add(edge[0]); // remove this line for DIRECTED graph
                }
               return  bfs(n ,source ,destination,adj);
    }
}
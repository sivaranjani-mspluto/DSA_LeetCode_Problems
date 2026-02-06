/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void utility(List<Integer> result,TreeNode root){
        if(root!=null){
            utility(result,root.left);
            result.add(root.val);
            utility(result,root.right);
        }
    }
    public boolean isValidBST(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        utility(result,root);

        for(int i=0;i<result.size()-1;i++){
            if(result.get(i)>=result.get(i+1)) return false;
        }
        return true;
    }
}
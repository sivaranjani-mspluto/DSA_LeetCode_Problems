class Solution {
    public static int[] solution(int a[],int n) {
		Stack<Integer> st= new Stack<>();
		int res[] = new int[n];
		for(int i= 2*n-1 ;i>=0;i--) {
            int indx = i%n;
			while(!st.isEmpty() && st.peek()<=a[indx]) {
				st.pop();
				
			}
			res[indx]=st.isEmpty() ? -1 : st.peek();
			st.push(a[indx]);
		}
		//for(int i=0;i<n;i++) System.out.print(a[i]+" ");
        return res;
    }
    public int[] nextGreaterElements(int[] nums) {
        int res[] = new int[nums.length];
        res= solution(nums,nums.length);
        return res;
    }
}
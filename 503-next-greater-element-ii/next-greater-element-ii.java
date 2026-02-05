class Solution {
    public static int[] solution(int a[],int n) {
		Stack<Integer> st= new Stack<>();
		int res[] = new int[n];
        Arrays.fill(res,-1); // TO FILL ALL THE ELEMENTS IN THE ARRAY AS -1 
		for(int i= 2*n ;i>=0;i--) {
            int indx = i%n;
			while(!st.isEmpty() && st.peek()<=a[indx]) {
				st.pop();
				
			}
            if(i<n)  res[indx]=st.isEmpty() ? -1 : st.peek(); // 
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
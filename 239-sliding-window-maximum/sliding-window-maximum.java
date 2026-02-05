class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq= new ArrayDeque<>();
        int n=nums.length;
        int[] res = new int[n-k+1];

        for(int i=0;i<n;i++){ // TRACK ELEMENTS 
        //[1,3,-1,-3,5,3,6,7]
        //DQ:0,I=1
            if(!dq.isEmpty() && dq.peekFirst()<= i-k)
                dq.pollFirst();
                 while (!dq.isEmpty() && nums[dq.peekLast()]<nums[i])
                    dq.pollLast(); //DECREASING
            dq.addLast(i);//DQ:0

            if (i>=k-1)
                res[i-k+1] = nums[dq.peekFirst()];
        }
            return res;
        }
}
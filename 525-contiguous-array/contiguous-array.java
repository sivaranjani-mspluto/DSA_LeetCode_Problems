class Solution {
    public int findMaxLength(int[] nums) {
        HashMap<Integer,Integer> mp= new HashMap<>();
        int sum =0, maxlen=0;
        for(int i=0;i<nums.length;i++) {
            if (nums[i]==0) sum--;
            else sum++;
            if (sum==0) maxlen=i+1;
            else if (mp.containsKey(sum)) maxlen=Math.max(maxlen,i-mp.get(sum));
            else mp.put(sum,i);
        }
        return maxlen;
    }
}
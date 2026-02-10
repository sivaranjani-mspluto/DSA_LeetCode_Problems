class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n= nums.length;
        int csum=nums[0]+nums[1]+nums[2];
        for(int i=0;i<n-2;i++){
            int low=i+1;
            int high = n-1;
            while(low<high){
                int sum= nums[i]+nums[low]+nums[high]; 
                if(Math.abs(target-sum)<Math.abs(target-csum))  csum=sum;
                if(sum>target) high--;
                else low++;
            }
        }
        return csum;
    }
}
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxc= 0;
        for(int i: candies){
            if (i>maxc) maxc=i;
        }
        ArrayList<Boolean> res= new ArrayList<>();
        for (int i:candies){
            if(i+extraCandies >=maxc) res.add(true);
            else res.add(false);
        }
        return res;

    }
}
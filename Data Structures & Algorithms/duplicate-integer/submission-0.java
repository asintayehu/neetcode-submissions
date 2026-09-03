class Solution {
    public boolean hasDuplicate(int[] nums) {
        // witerally make a hash map
        HashMap<Integer, Integer> map = new HashMap<>();
        // map array element to number of appearances
        for(int i = 0; i < nums.length; i++){
            // ( key : value )
            // check if key exists
            if(map.containsKey(nums[i])){
                return true;
            } else {
                map.put(nums[i], 1);
            }
        }

        return false;

        
    }
}
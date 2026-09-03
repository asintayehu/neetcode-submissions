class Solution {
    public boolean isAnagram(String s, String t) {
        // given a string S, T
        // return true if two strings are anagrams of each other
        // return false otherwise
        /**
            Strat: Create 2 hashmaps. One for S, One for T.
                   HashMap should map character to # of appearances
                   # Compare hash maps
                   # If one occurance not match -> false
                   # otherwise return true
        **/

        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> s_map = new HashMap<>();
        HashMap<Character, Integer> t_map = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            if(s_map.get(s.charAt(i)) != null){
                // increment
                s_map.put(s.charAt(i), s_map.get(s.charAt(i))+1);
            } else { 
                s_map.put(s.charAt(i), 1);
            }
        }

        for(int i = 0; i < t.length(); i++){
            if(t_map.get(t.charAt(i)) != null){
                // increment
                t_map.put(t.charAt(i), t_map.get(t.charAt(i))+1);
            } else { 
                t_map.put(t.charAt(i), 1);
            }
        }


        return s_map.equals(t_map);

    }
}
